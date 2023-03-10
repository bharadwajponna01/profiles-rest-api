from rest_framework import serializers
from profiles_api.models import UserProfile


class HelloSerializer(serializers.Serializer):
    """ serializers a name field for testing our apiview """
    name = serializers.CharField(max_length=40)


class UserProfileSerializer(serializers.ModelSerializer):
    """ serializer a user profile object """
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
              'write_only': True,
              'style': {'input_type': 'password'}

            }
        }

    def create(self, validated_data):
        """ create and return a new user """
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user