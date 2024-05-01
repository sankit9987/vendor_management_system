from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from vendors.serializers import VendorSerializer, VendorPerformanceSeriaizer
from vendors.models import Vendor


class VendorListCreateAPIView(ListCreateAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    permission_classes = [IsAuthenticated]


class VendorDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    permission_classes = [IsAuthenticated]


class VendorPerformanceAPIView(RetrieveAPIView):
    serializer_class = VendorPerformanceSeriaizer
    queryset = Vendor.objects.all()
    permission_classes = [IsAuthenticated]
