from django.contrib import admin
from django.urls import path
from orders import views
urlpatterns = [
    path('', views.OrderListCreateAPIView.as_view(), name="order_list_create"),
    path('/<int:pk>', views.OrderDetailUpdateDeleteAPIView.as_view(), name="orders_detail_update_delete"),
]