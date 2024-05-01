from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from orders.serializers import OrdersSerializer
from orders.models import Order
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import datetime


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class OrderDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class VendoreAcknowledgedAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs.get("pk")
        if order_id is not None:
            order = Order.objects.get(id=order_id)
            order.acknowledged_date = datetime.datetime.now()
            order.save()
            return Response(
                {"message": f"Order acknowledged by {order.vendor.name}"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Order Id is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )
