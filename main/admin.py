from django.contrib import admin
#from main.models import Person
#Данный импорт нужен для того, чтобы наша таблица отображалась в admin панеле
from main.models import Categories, Products

#admin.site.register(Categories)
#admin.site.register(Products)

"""
В данном классе можно настроить тонкую настройку отображения
информации в admin панеле
"""

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('name',)}
    fields_display=('name',)
    ordering=('name',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('name',)}
    ordering=('name',)


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
# display= ('name', 'surname',)
# serch_fields=('name', 'surname',)
# ordering=('name',)
# # Register your models here.

