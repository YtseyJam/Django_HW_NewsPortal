from django.contrib import admin
from .models import Post, Category, Author
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки
# Register your models here.

class PostAdmin(TranslationAdmin):
    model = Post
class AuthorAdmin(TranslationAdmin):
    model = Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
