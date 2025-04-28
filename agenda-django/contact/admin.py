from contact import models
from django.contrib import admin


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = 'id', 'first_name', 'last_name', 'phone', 'show'
  ordering = 'id', # Se eu precisar que seja decrescente é só colocar o - (-id)
  # list_filter = 'created_date' = lista de filtros, posso adicionar varios so separando por virgula
  search_fields = 'id', 'first_name', 'last_name', # adiciono o campo de busca
  list_per_page = 10 # quantidade de registros por pagina
  list_max_show_all = 200 # quantidade maximo de registros para ver todos
  list_editable = 'first_name', 'last_name', 'show' # campos que podem ser editados
  list_display_links = 'id', 'phone', # campos que podem ser clicados

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = 'name',
  ordering = 'id', # Se eu precisar que seja decrescente é só colocar o -