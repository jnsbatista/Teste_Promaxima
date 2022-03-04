from django.urls import path

from . import views

urlpatterns = [
    path('', views.dataList, name='data-list'),
    path('newgasolina', views.newGasolina, name='new-gasolina'),
    path('edite/<int:id>', views.editGasolina, name='edit-gasolina'),
    path('delete/<int:id>', views.deleteGasolina, name='delete-gasolina'),
    path('colectdata', views.colectData, name='colect-data'),
]
