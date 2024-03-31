from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.contrib.sitemaps.views import index, sitemap
from django.urls import include, path
from django.urls import re_path as url

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^terms-of-use/$", flatpage, {"url": "/terms-of-use/"}, name="terms"),
    url(r"^privacy-policy/$", flatpage, {"url": "/privacy-policy/"}, name="privacy-policy"),
    path("", include("shop.urls")),
]
