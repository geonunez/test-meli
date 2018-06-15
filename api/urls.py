# -*- coding: utf-8 -*-

"""
Api's Urls
"""

from django.conf.urls import url

from .views import HumanViewSet

urlpatterns = [
    url(r'^mutant$', HumanViewSet.as_view({'post': 'is_mutant'})),
    url(r'^stats$', HumanViewSet.as_view({'get': 'stats'})),
]
