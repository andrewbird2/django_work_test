from django.conf.urls import url, include

from .api import router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = "crm"
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
