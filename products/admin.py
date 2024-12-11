from django.contrib import admin
from .models import Product, Test
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active','category']
    list_display_links =['name', 'price']
    list_editable =['category','active']
    search_fields=['name']
    list_filter = ['category', 'price']
    #fields =['name', 'price']
admin.site.register(Product, ProductAdmin)
admin.site.register(Test)
admin.site.site_header = 'asmaa'
admin.site.site_title = 'asmaa'