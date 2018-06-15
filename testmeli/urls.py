from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

from api.views import IndexViewSet

schema_view = get_swagger_view(title='Geonunez Test-Meli')

urlpatterns = [
    url(r'^$', IndexViewSet.as_view({'get': 'index'}), name='index'),
    url(r'^api/doc$', schema_view),
    url(r'^api/v1/', include('api.urls'))
]
