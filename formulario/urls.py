
from django.contrib import admin
from django.urls import path,include
from formularioContratacao.views import index, form, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
]
