from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from amicci_briefing.api import views


urlpatterns = [
    path("briefings/", views.ListBriefings.as_view()),
    path("retailers/", views.ListRetailers.as_view()),
    path("vendors/", views.ListVendors.as_view()),
    path("categories/", views.ListCategories.as_view()),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
        ),
        name="swagger-ui",
    ),
]

urlpatterns += staticfiles_urlpatterns()
