from django.contrib import admin
from .models import Briefing, Retailer, Vendor, Category

# Register your models here.
admin.site.register(Briefing)
admin.site.register(Retailer)
admin.site.register(Vendor)
admin.site.register(Category)
