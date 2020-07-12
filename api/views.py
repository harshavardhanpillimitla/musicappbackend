from rest_framework import viewsets,permissions
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics,filters

from api.models import User,Song,PlaylistAddedsongs,Userplaylist,PlaylistPermission
from rest_framework.response import Response
from .serializer import UserSerializer,SongSerializer,PlaylistAddedsongsSerializer,UserplaylistSerializer,PlaylistpermissionSerializer,PlaylistsongslistSerializer


class UserViewSet(viewsets.ModelViewSet):
  
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]



 


# class PostViewset(viewsets.ModelViewSet):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [permissions.IsAuthenticated]
    
 
        
    
#     serializer_class=PostSerializer
#     def perform_create(self, serializer):
        
#         serializer.save(user=self.request.user)

#     def get_queryset(self):
        
#         if self.request.user.is_superuser:
#             return Post.objects.all()

#         return Post.objects.all().filter(user=self.request.user)

class SongViewSet(viewsets.ModelViewSet):
    search_fields = ['song_name']
    filter_backends = (filters.SearchFilter,)  
    
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    


class UserplaylistViewSet(viewsets.ModelViewSet):

    serializer_class = UserplaylistSerializer

    # queryset = Userplaylist.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        if(PlaylistPermission.objects.filter(user_permitted = self.request.user )):

            b= PlaylistPermission.objects.filter(user_permitted = self.request.user )[0].playlist
            
        
            a= Userplaylist.objects.all().filter(Q(user=self.request.user) | Q(playlist_name = b))
            
            return a
    

        return Userplaylist.objects.all()


class PlaylistAddedsongsViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistAddedsongsSerializer
    
    queryset = PlaylistAddedsongs.objects.all()


class playlistsongsview(viewsets.ModelViewSet):
    
    
    serializer_class= PlaylistsongslistSerializer
    queryset=PlaylistAddedsongs.objects.all()


    
class PlaylistPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistpermissionSerializer
    queryset = PlaylistPermission.objects.all()



    

                      
