from rest_framework import generics, mixins
from .models import Briefing, Retailer, Vendor, Category
from .serializers import (
    BriefingSerializer,
    CategorySerializer,
    RetailerSerializer,
    VendorSerializer,
)

# Briefing
class BriefingListView(generics.ListAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer


# Retailer
class RetailerListView(generics.ListAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


# Vendor
class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorCreateView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# Category
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
