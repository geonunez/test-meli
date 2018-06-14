'''
Api's Urls
'''

from django.conf.urls import url

from .views import MutantViewSet

urlpatterns = [
    url(r'^mutant$', MutantViewSet.as_view({
        'post': 'is_mutant'
    })),
]
