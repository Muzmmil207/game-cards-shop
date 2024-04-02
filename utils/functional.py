from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest


def get_url(request=None):
    request = request or HttpRequest()
    # to get the domain of the current site
    domain = get_current_site(request).domain
    return "{0}://{1}".format(request.scheme, domain)


def get_full_url(request=None):
    request = request or HttpRequest()
    return get_url(request) + "{0}".format(request.get_full_path())
