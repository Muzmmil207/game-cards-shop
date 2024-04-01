from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.contrib.sitemaps.views import index, sitemap
from django.urls import include, path
from django.urls import re_path as url

urlpatterns = [
    path("admin/", admin.site.urls),
    # THIRD_PARTY_APPS_URLs
    path("", include("allauth.urls")),
    #
    url(r"^terms-of-use/$", flatpage, {"url": "/terms-of-use/"}, name="terms"),
    url(r"^privacy-policy/$", flatpage, {"url": "/privacy-policy/"}, name="privacy-policy"),
    #
    path("cart/", include("apps.cart.urls")),
    path("payment/", include("apps.payment.urls")),
    path("account/", include("apps.accounts.urls")),
    path("", include("apps.base.urls")),
    path("", include("apps.shop.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
