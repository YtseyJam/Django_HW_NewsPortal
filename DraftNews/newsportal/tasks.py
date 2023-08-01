from celery import shared_task
import datetime
import time
from newsportal.models import Post, Category
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@shared_task
def send_notifications(preview, pk, post_title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=post_title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_context, "text/html")
    msg.send()


@shared_task()
def weekly_notification():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)  #точка отсчета -- "неделя назад"
    posts = Post.objects.filter(post_datetime__gte=last_week)
    categories = set(posts.values_list('categories__category', flat=True))  #flat=True преобразует словарь в список строк
    #оборачиваем в множество, чтобы не дублировались категории
    subscribers = set(Category.objects.filter(category__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,

        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='', #т.к. есть шаблон
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()