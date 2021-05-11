from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework import permissions

from recipes.models import Recipe
from recipes.serializers import UserSerializer, GroupSerializer, RecipeSerializer


class Website(View):
    def index(self):
        all_recipes = Recipe.objects.all()
        return render(self, 'recipes/index.html', {'all_recipes': all_recipes})

    def recipe(self, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return render(self, 'recipes/recipe_view.html', {'recipe': recipe})

    def new(self):
        return render(self, 'recipes/recipe_new.html', {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipe to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
