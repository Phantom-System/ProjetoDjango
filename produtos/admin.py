from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Produto)