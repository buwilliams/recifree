from django.urls import path, include
from rest_framework import routers

from . import views
from .views import Website

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = [
    path('', Website.index, name='index'),
    path('recipes/<int:recipe_id>', Website.recipe, name='recipe'),
    path('recipes/new', Website.new, name='recipe_new'),

    path('recipes/homepage', Website.homepage, name='homepage'),

    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]