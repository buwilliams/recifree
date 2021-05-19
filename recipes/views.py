from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework import permissions

from recipes.models import Recipe
from recipes.serializers import UserSerializer, GroupSerializer, RecipeSerializer


class Website:
    @staticmethod
    def index(request):
        is_authenticated = request.user.is_authenticated
        all_recipes = Recipe.objects.all()
        return render(request, 'recipes/index.html', {
            'all_recipes': all_recipes,
            'is_authenticated': is_authenticated,
        })

    @staticmethod
    def recipe(request, recipe_id):
        is_authenticated = request.user.is_authenticated
        recipe_object = Recipe.objects.get(id=recipe_id)
        return render(request, 'recipes/recipe_view.html', {
            'recipe': recipe_object,
            'is_authenticated': is_authenticated,
        })

    @staticmethod
    def new(request):
        is_authenticated = request.user.is_authenticated
        return render(request, 'recipes/recipe_new.html', {
            'is_authenticated': is_authenticated,
        })

    @staticmethod
    def profile(request, username):
        is_authenticated = request.user.is_authenticated
        users = User.objects.filter(username=username)
        if users:
            user = users[0]
            recipes = user.recipe_set
            return render(request, 'recipes/profile.html', {
                'is_authenticated': is_authenticated,
                'recipes': recipes.all(),
                'username': user.username
            })
        else:
            return render(request, 'recipes/profile.html', {
                'is_authenticated': is_authenticated,
                'recipes': [],
                'username': username
            })


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
