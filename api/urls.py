from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api.views import UserViewSet,PostViewset

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'post', PostViewset,basename='post')

urlpatterns = [url(r'^', include(router.urls)),
url(r'^auth/', include('rest_auth.urls')),
]