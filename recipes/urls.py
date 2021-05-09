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
    path('recipes/<int:id>', Website.recipe, name='recipe'),

    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]