from tabnanny import verbose
from unicodedata import category
from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value <= 0:
        raise ValidationError(
_('%(value)s Количество рецептов не должно быть отрицательным'),
params={'value': value},
)

class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=100)
    description = models.TextField(verbose_name='Описание категории')
    amount = models.IntegerField(verbose_name='Количество рецептов', validators=[validate_even])

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural ='Категории'

class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=100)
    email = models.CharField(verbose_name='Почта', max_length=100)
    recipes = models.IntegerField(verbose_name='Количество написаных рецептов')
    about = models.TextField(verbose_name='Об авторе')
    bset_categoty = models.ManyToManyField(Category, verbose_name='Лучшая категория')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Автор'
        verbose_name_plural ='Авторы'

class Recipe(models.Model):
    recipe_title = models.CharField(verbose_name='Рецепт', max_length=100)
    ingredients = models.TextField(verbose_name='Ингредиенты')
    time = models.FloatField(verbose_name='Время приготовления')
    persons = models.IntegerField(verbose_name='Порций')
    category= models.ManyToManyField(Category, verbose_name='Категория')
    autor = models.ManyToManyField(Author, verbose_name='Автор')
 
    history = HistoricalRecords()

    def __str__(self):
        return self.recipe_title

    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural ='Рецепты'