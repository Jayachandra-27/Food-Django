from django.contrib import admin

from foodapp.models import Category, Make, Menu

# Register your models here.

admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Make)
