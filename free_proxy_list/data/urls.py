from django.urls import path

from . import views

urlpatterns = [
    path('', views.dataList, name='data-list'),
    path('newproxy', views.newProxy, name='new-proxy'),
    path('edite/<int:id>', views.editProxy, name='edit-proxy'),
    path('delete/<int:id>', views.deleteProxy, name='delete-proxy'),
    path('colectdata', views.colectData, name='colect-data'),
]
