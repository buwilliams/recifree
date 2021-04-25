from django.contrib.auth.models import User, Group
from rest_framework import serializers

from recipes.models import Recipe


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['pk', 'author', 'title', 'description', 'photo_url', 'video_url', 'instructions', 'ingredients']
