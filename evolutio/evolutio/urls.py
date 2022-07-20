from django.contrib import admin
from django.urls import path
from test_api import api_views, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders', api_views.OrderListView.as_view()),
    path('api/products', api_views.ProductQuantityListView.as_view()),
    path('api/docs', views.OpenApiView.as_view())
]
