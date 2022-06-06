from urllib.request import Request
from rest_framework.viewsets import ModelViewSet
from .serializers import AutorSerializer, RecipeSerializer, CategorySerializer
from .models import Author, Category, Recipe
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryViewSet(ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    @action(methods=['Delete'], detail=True, url_path='delCat') 
    def delCategory(self,request, pk=None):
        category=self.queryset.get(id=pk)
        category.delete()
        return Response('Succses')

class AuthorViewSet(ModelViewSet):
    queryset= Author.objects.all()
    serializer_class=AutorSerializer

class GetAuthorView(ListAPIView):
    queryset = Author.objects.filter( Q(recipe__gt=21) | Q(name='Данила Гусев'))
    serializer_class = AutorSerializer


class RecipeViewSet(ModelViewSet):
    queryset= Recipe.objects.all()
    serializer_class=RecipeSerializer

class GetRecipeView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['persons','time']
