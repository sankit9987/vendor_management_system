from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from orders.serializers import OrdersSerializer
from orders.models import Order


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()

    
class OrderDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()