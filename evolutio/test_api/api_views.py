from rest_framework.generics import ListAPIView
from rest_framework.exceptions import NotFound
from django.db.models import Sum

from test_api import models, serializers
from test_api.paginators import CursorOrderPagination


class OrderListView(ListAPIView):
    """
    ListAPI for retrieving orders info and its deliveries by brand_id
    """

    serializer_class = serializers.OrderSerializer
    pagination_class = CursorOrderPagination

    def get_queryset(self):
        """
        Method overridden to include brand_id query param filtering
        """

        queryset = None

        brand_id = self.request.query_params.get('brand_id')

        if brand_id and brand_id.isdigit():
            queryset = models.Order.objects.filter(brand_id=int(brand_id))

        if queryset:
            return queryset

        raise NotFound()


class ProductQuantityListView(ListAPIView):
    """
    ListAPI for retrieving quantity of product of each type and its name by reference or id
    """

    serializer_class = serializers.ProductQuantitySerializer

    def get_queryset(self):
        """
        Method overridden to include reference/id query param filtering
        """

        queryset = None

        reference = self.request.query_params.get('reference')
        order_id = self.request.query_params.get('id')

        if reference:
            queryset = self.get_query_by_order_reference(reference)

        if order_id and order_id.isdigit():
            queryset = self.get_query_by_order_id(int(order_id))

        if queryset:
            return queryset

        raise NotFound()

    def get_query_by_order_reference(self, order_reference):

        return models.Product.objects.filter(delivery__shipped=True,
                                             delivery__order_FK__reference=order_reference).values('name').annotate(
            quantity=Sum('product_delivery_product__quantity'))

    def get_query_by_order_id(self, order_id):

        return models.Product.objects.filter(delivery__shipped=True, delivery__order_FK__id=order_id).values(
            'name').annotate(quantity=Sum('product_delivery_product__quantity'))




