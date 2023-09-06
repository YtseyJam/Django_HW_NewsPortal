from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

from django.core.cache import cache

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy # импортируем «ленивый» геттекст с подсказкой

class Author(models.Model):

    user_rating = models.IntegerField(default=0) #default = 0.0 ?
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        """
        *cуммарный рейтинг каждой статьи автора умножается на 3;
        *суммарный рейтинг всех комментариев автора;
        *суммарный рейтинг всех комментариев к статьям автора
        """

        postRat = self.post_set.all().aggregate(postRating=Sum('post_rating'))
        pRat = 0
        pRat += postRat.get("postRating")

        commentAutRat = self.user.comment_set.all().aggregate(commentAutRating=Sum('comm_rating'))
        cRat = 0
        cRat += commentAutRat.get('commentAutRating')


        cuRat = 0

        for i in range(len(self.post_set.all())-1):
            com_us_rat = self.post_set.all()[i].comment_set.all().aggregate(commRates=Sum('comm_rating'))
            cuRat += com_us_rat.get('commRates')


        self.user_rating = pRat *3 + cRat + cuRat
        self.save()



humor = "HUM"
politics = "POL"
science = "SCI"
sport = "SPT"
arts = "ART"

news = 'NEWS'
article = 'ARTL'

CATEGORIES = [
    (humor, 'Юмор'),
    (politics, 'Политика'),
    (science, 'Наука'),
    (sport, 'Спорт'),
    (arts, 'Искусство')
]

TYPES = [
    (news, 'Новость'),
    (article, "Статья")
]



class Category(models.Model):
    category = models.CharField(max_length = 3, choices=CATEGORIES, unique = True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.category

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length=4, choices=TYPES) #news or article
    post_datetime = models.DateTimeField(auto_now_add = True)
    post_title = models.CharField(max_length=64, help_text=_('title of the post'))
    post_body = models.TextField()
    post_rating = models.IntegerField(default=0) #default = 0.0 ?
    categories = models.ManyToManyField(Category, through = "PostCategory")

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_body[:124]}. {self.post_type}'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_body[:124] + "..."

    def get_absolute_url(self):
        return reverse('exactly_news', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.post.post_title} | {self.category.category}'

# class Subscription(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='subscriptions',
#     )
#     post_type = models.ForeignKey(
#         to=Post,
#         on_delete=models.CASCADE,
#         related_name='subscriptions',
#     )


class Comment(models.Model):
    comm_text = models.TextField()
    comm_datetime = models.DateTimeField(auto_now_add = True)
    comm_rating = models.FloatField(default = 0.0)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def like(self):
        self.comm_rating += 1
        self.save()


    def dislike(self):
        self.comm_rating -= 1
        self.save()