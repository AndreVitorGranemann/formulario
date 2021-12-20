from django.urls import path
<<<<<<< HEAD
from . import views
=======
from . import views 
>>>>>>> 62b0197 (alteracao)

urlpatterns = [
    path('', views.index, name='index'),
    path('sucesso', views.sucesso, name='sucesso'),
<<<<<<< HEAD
=======
    path('create', views.create, name='create')
>>>>>>> 62b0197 (alteracao)
]