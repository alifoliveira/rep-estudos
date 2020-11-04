from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('newpost/', views.newpost, name='new-post'),
    path('editpost/<int:id>', views.editpost, name='edit-post'),
    path('deletepost/<int:id>', views.deletepost, name='delete-post'),
    path('about/', views.about, name='about'),
]
