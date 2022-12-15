from .models import Briefing, Retailer, Vendor, Category
from rest_framework import serializers


class BriefingSerializer(serializers.ModelSerializer):
    retailer = serializers.ReadOnlyField(source="retailer.name")
    category = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Briefing
        fields = "__all__"


class BriefingCreateSerializer(serializers.ModelSerializer):
    retailer = serializers.PrimaryKeyRelatedField(queryset=Retailer.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Briefing
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class RetailerSerializer(serializers.ModelSerializer):
    vendors = VendorSerializer(many=True)

    class Meta:
        model = Retailer
        fields = ("name", "vendors")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
