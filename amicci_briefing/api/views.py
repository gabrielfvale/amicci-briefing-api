from rest_framework import generics, mixins
from .models import Briefing, Retailer, Vendor, Category
from .serializers import (
    BriefingSerializer,
    CategorySerializer,
    RetailerSerializer,
    VendorSerializer,
)


class ListBriefings(generics.ListAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer


class ListRetailers(generics.ListAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


class ListVendors(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ListCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
