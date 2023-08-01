from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import NewsForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

#celery tasks
from django.http import HttpResponse
from django.views import View
from .tasks import hello

from django.core.cache import cache #кэш


@method_decorator(login_required, name='dispatch')
class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'post_datetime'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'all_news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10 #вот так мы можем указать количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-post_datetime')
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        context['filterset'] = self.filterset

        context['is_author'] = self.request.user.groups.filter(name='authors').exists()

        return context

@login_required
def upgrade_user(request):
    user = request.user
    group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        group.user_set.add(user)
        Author.objects.create(user=user)
    return redirect('/news')


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'exactly_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'exactly_news'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj

class NewsSearch(NewsList):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news_search'

class NewsCreate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsportal.add_post',)  #<app>.<action>_<model>

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NEWS'
        return super().form_valid(form)

class ArtlCreate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsportal.add_post',)  # <app>.<action>_<model>

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'ARTL'
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('newsportal.change_post',)

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newsportal.delete_post',)

    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class CategoryListView(ListView):
    """ при нажатии на категорию выводит список постов этой категории с возможностью подписаться на оную"""
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'
    paginate_by = 10

    def get_queryset(self):
        self.categories = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categories=self.categories).order_by('-post_datetime')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.categories.subscribers.all()
        context['category'] = self.categories
        return context

@csrf_protect
@login_required()
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = f'{user.username.capitalize()}, вы успешно подписались на рассылку в категории 👉{str(category).upper()}'
    return render(request, 'subscribe.html', {'message': message})

@csrf_protect
@login_required()
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = f'{user.username.capitalize()}, вы успешно отписались от рассылки в категории 🚫{str(category).upper()}'
    return render(request, 'unsubscribe.html', {'message': message})

#Celery task
class IndexView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('Hello!')