from django.contrib import admin
from .models import Orders, Goods


class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("counter_party",)}


admin.site.register(Orders, OrderAdmin)


class GoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Goods, GoodAdmin)
