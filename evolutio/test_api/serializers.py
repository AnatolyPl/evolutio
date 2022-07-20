from rest_framework import serializers
from test_api import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ['name']


class DeliveryProductSerializerGlue(serializers.ModelSerializer):

    product_name = ProductSerializer(source='product_FK')

    class Meta:
        model = models.DeliveryProduct
        fields = ['product_name', 'quantity']

    def to_representation(self, obj):
        """Move fields from product to delivery representation."""

        representation = super().to_representation(obj)
        profile_representation = representation.pop('product_name')
        for key in profile_representation:
            representation[key] = profile_representation[key]

        return representation


class DeliverySerializer(serializers.ModelSerializer):

    products = DeliveryProductSerializerGlue(many=True, source='delivery_delivery_product')

    class Meta:
        model = models.Delivery
        fields = ['id', 'shipped', 'products']


class OrderSerializer(serializers.ModelSerializer):

    deliveries = DeliverySerializer(many=True, read_only=True, source='delivery_set')

    class Meta:
        model = models.Order
        fields = ['id', 'brand_id', 'reference', 'date_of_creation', 'price_total', 'deliveries']


class ProductQuantitySerializer(serializers.ModelSerializer):
    """
    Serializer for aggregated quantity of each product in order
    """

    quantity = serializers.IntegerField()

    class Meta:
        model = models.Product
        fields = '__all__'
