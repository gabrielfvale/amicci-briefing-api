from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from amicci_briefing.api import views


urlpatterns = [
    # Briefing
    path("briefings/", views.BriefingListView.as_view()),
    path("briefing/<int:pk>", views.BriefingRetrieveUpdateView.as_view()),
    path("briefing/", views.BriefingCreateView.as_view()),
    # Retailer
    path("retailers/", views.RetailerListView.as_view()),
    path("retailer/<int:pk>", views.RetailerRetrieveUpdateView.as_view()),
    path("retailer/", views.RetailerCreateView.as_view()),
    # Vendor
    path("vendors/", views.VendorListView.as_view()),
    path("vendor/<int:pk>", views.VendorRetrieveUpdateView.as_view()),
    path("vendor/", views.VendorCreateView.as_view()),
    # Category
    path("categories/", views.CategoryListView.as_view()),
    path("category/<int:pk>", views.CategoryRetrieveUpdateView.as_view()),
    path("category/", views.CategoryCreateView.as_view()),
    # Other
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
        ),
        name="swagger-ui",
    ),
]

urlpatterns += staticfiles_urlpatterns()
