from django.contrib import admin
from .models import Projetos

# Register your models here.

@admin.register(Projetos)
class AdminContent(admin.ModelAdmin):
  list_display = ('image', 'title', 'description', 'linkProject', 'linkRepo')
