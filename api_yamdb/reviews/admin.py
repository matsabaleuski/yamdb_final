from django.contrib import admin

from .models import Category, Genre, Genre_Title, Title

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Genre_Title)
admin.site.register(Title)
