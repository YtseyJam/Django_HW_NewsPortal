import django_filters
from django_filters import FilterSet, DateTimeFilter, CharFilter, DateFilter
from django.forms import DateTimeInput
from .models import Post

class PostFilter(FilterSet):
    post_title = django_filters.CharFilter(lookup_expr='icontains', label='По заголовку')
    added_after = DateTimeFilter(
        field_name='post_datetime',
        lookup_expr='gt',
        label="После даты",
        widget = DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )


    class Meta:
        model = Post

        fields = {
            #"post_title": ['icontains'],
            "categories": ['exact'],
        }
