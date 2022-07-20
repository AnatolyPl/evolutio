from django.contrib import admin
from test_api import models


class OrderAdmin(admin.ModelAdmin):

    list_display = ['get_customer_name', 'brand_id', 'reference']

    def get_customer_name(self, obj):

        return obj.customer_FK.first_name

    get_customer_name.short_description = 'Customer Name'


class DeliveryProductAdmin(admin.ModelAdmin):

    list_display = ['get_product_name', 'quantity']

    def get_product_name(self, obj):

        return obj.product_FK.name

    get_product_name.short_description = 'Product Name'


admin.site.register(models.Delivery)
admin.site.register(models.Product)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Customer)
admin.site.register(models.DeliveryProduct, DeliveryProductAdmin)
