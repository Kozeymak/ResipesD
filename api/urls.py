from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, RecipeViewSet, CategoryViewSet, GetAuthorView, GetRecipeView
router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('author', AuthorViewSet)
router.register('recipe', RecipeViewSet)

urlpatterns = [
    path ('api/', include(router.urls)),
    path('api/author/filters', GetAuthorView.as_view()),
    path('api/recipe/filters', GetRecipeView.as_view()),
]