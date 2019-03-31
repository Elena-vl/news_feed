from django.contrib import admin

from .models import Category
from .models import Articles

admin.site.register(Category)
admin.site.register(Articles)