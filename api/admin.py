from weakref import proxy
from django.contrib import admin
from .models import Author, Category, Recipe
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class author(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Category)
class category(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Recipe)
class recipe(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True