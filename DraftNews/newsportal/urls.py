from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, ArtlCreate, CategoryListView, \
   subscribe, upgrade_user, unsubscribe, IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   # path('', cache_page(60*5)(NewsList.as_view()), name='news_list'), #кэшируется шапка -- не подходит
   path('', NewsList.as_view(), name='news_list'),

# pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', NewsDetail.as_view(), name='exactly_news'),
   path('search/', NewsSearch.as_view(), name='news_search'),

   path('create/', NewsCreate.as_view(), name='news_edit'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

   path('articles/create/', ArtlCreate.as_view(), name='artl_edit'),
   path('articles/<int:pk>/update/', NewsUpdate.as_view(), name='artl_update'),
   path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='artl_delete'),
   # path('subscriptions/', subscriptions, name='subscriptions'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),  #не указываем as_view, т.к. это функция
   path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
   path('upgrade/', upgrade_user, name='account_upgrade'),
   path('task', IndexView.as_view()),
]

