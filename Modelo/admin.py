from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
 
    list_display = ['nome', 'idade']
    