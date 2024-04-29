from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from vendors.serializers import VendorSerializer
from vendors.models import Vendor


class VendorListCreateAPIView(ListCreateAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

    
class VendorDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()