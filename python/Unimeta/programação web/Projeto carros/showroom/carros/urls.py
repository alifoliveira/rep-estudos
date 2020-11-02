from django.urls import path, include
from . import views

# rotas
urlpatterns = [
    path('', views.index, name='index'),
    path('pagina', views.pagina, name='pagina'),
]
