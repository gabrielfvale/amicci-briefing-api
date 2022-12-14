from django.urls import path, include
from rest_framework import routers
from amicci_briefing.api import views

router = routers.DefaultRouter()
# router.register(r"briefing", views.BriefingViewSet)
# router.register(r"retailer", views.RetailerViewSet)
# router.register(r"vendor", views.VendorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
