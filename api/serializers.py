from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Author, Recipe, Category

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'