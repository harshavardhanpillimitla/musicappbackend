from rest_framework import serializers
from api.models import User,Song,Userplaylist,PlaylistAddedsongs,PlaylistPermission
import json
from rest_framework import generics




class UserSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)


        user.save()
        
        return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     profile = instance.profile

    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     profile.title = profile_data.get('title', profile.title)
    #     profile.dob = profile_data.get('dob', profile.dob)
    #     profile.address = profile_data.get('address', profile.address)
    #     profile.country = profile_data.get('country', profile.country)
    #     profile.city = profile_data.get('city', profile.city)
    #     profile.zip = profile_data.get('zip', profile.zip)
    #     profile.photo = profile_data.get('photo', profile.photo)
    #     profile.save()

    #     return instance



# class PostSerializer(serializers.ModelSerializer):
   
    
#     # def create(self,validated_data):
        
        

#     #     post=Post.objects.create(
#     #         user = self.request.user,
#     #         name = validated_data['name'],
#     #         latitude= validated_data['latitude'],
#     #         longitutude= validated_data['longitutude'],
#     #         picture = validated_data['picture']
#     #     )
        
#     #     post.save()
#     #     return post

#     class Meta:
#         model = Post
#         fields = ['id','name','latitude','longitutude','picture']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'


class UserplaylistSerializer(serializers.ModelSerializer):
    class Meta:
        
        model =  Userplaylist
        fields=['playlist_name','id']
   


class PlaylistAddedsongsSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = PlaylistAddedsongs
        fields = '__all__'


class PlaylistsongslistSerializer(serializers.ModelSerializer):
    playlist_name = UserplaylistSerializer()
    playlistsongs = SongSerializer(many=True)
    class Meta:
        model = PlaylistAddedsongs
        fields = '__all__'
   


class PlaylistpermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistPermission
        fields = '__all__'
    
   
