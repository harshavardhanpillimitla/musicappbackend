from rest_framework import viewsets,permissions
from rest_framework.parsers import MultiPartParser, FormParser

from api.models import User,Post
from rest_framework.response import Response
from .serializer import UserSerializer,PostSerializer


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



 


class PostViewset(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    
 
        
    
    serializer_class=PostSerializer
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)

    def get_queryset(self):
        
        if self.request.user.is_superuser:
            return Post.objects.all()

        return Post.objects.all().filter(user=self.request.user)


    

                      
