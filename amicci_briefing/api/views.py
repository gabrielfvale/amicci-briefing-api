from rest_framework import generics
from .models import Briefing, Retailer, Vendor, Category
from .serializers import (
    BriefingSerializer,
    BriefingCreateSerializer,
    CategorySerializer,
    RetailerSerializer,
    RetailerCreateSerializer,
    VendorSerializer,
)

# Briefing
class BriefingListView(generics.ListAPIView):
    queryset = Briefing.objects.all().order_by("id")
    serializer_class = BriefingSerializer


class BriefingCreateView(generics.CreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingCreateSerializer


class BriefingRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Briefing.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return BriefingCreateSerializer
        return BriefingSerializer


# Retailer
class RetailerListView(generics.ListAPIView):
    queryset = Retailer.objects.all().order_by("id")
    serializer_class = RetailerSerializer


class RetailerCreateView(generics.CreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerCreateSerializer


class RetailerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Retailer.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return RetailerCreateSerializer
        return RetailerSerializer


# Vendor
class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all().order_by("id")
    serializer_class = VendorSerializer


class VendorCreateView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# Category
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
