from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from amicci_briefing.api import views


urlpatterns = [
    # Briefing
    path("briefings/", views.BriefingListView.as_view()),
    # Retailer
    path("retailers/", views.RetailerListView.as_view()),
    # Vendor
    path("vendors/", views.VendorListView.as_view()),
    # Category
    path("categories/", views.CategoryListView.as_view()),
    path("category/<int:pk>", views.CategoryDetailUpdateView.as_view()),
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
