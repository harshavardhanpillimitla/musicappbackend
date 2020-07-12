from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api.views import UserViewSet,SongViewSet,UserplaylistViewSet,PlaylistAddedsongsViewSet,PlaylistPermissionViewSet,playlistsongsview

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename="users")
router.register(r'song', SongViewSet,basename="song")
router.register(r'createplaylist',  UserplaylistViewSet,basename="createplaylist")
router.register(r'addtoplaylist', PlaylistAddedsongsViewSet,basename="addtoplaylist")
router.register(r'follow', PlaylistPermissionViewSet,basename="follow")
router.register(r'playlist', playlistsongsview,basename="playlist")



urlpatterns = [url(r'^', include(router.urls)),
url(r'^auth/', include('rest_auth.urls')),
# path('playlist/<int:pk>/', playlistsongsview.as_view())
]


# router.register(r'post', PostViewset,basename='post')