from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('pokemon/',views.pokemon_index,name='index'),
    path('pokemon/<int:pokemon_id>/',views.pokemon_details,name='details'),
    path('pokemon/create/',views.PokemonCreate.as_view(),name='pokemon_create'),
    path('pokemon/<int:pk>/update/',views.PokemonUpdate.as_view(),name='pokemon_update'),
    path('pokemon/<int:pk>/delete/',views.PokemonDelete.as_view(),name='pokemon_delete'),
    path('pokemon/<int:pokemon_id>/add_purchase/',views.add_purchase,name='add_purchase'),
    
    path('accessory/',views.AccessoryList.as_view(), name= 'accessory_index'),
    path('accessory/<int:pk>/',views.AccessoryDetail.as_view(), name= 'accessory_detail'),
    path('accessory/create/',views.AccessoryCreate.as_view(), name= 'accessory_create'),
    path('accessory/<int:pk>/update/',views.AccessoryUpdate.as_view(), name= 'accessory_update'),
    path('accessory/<int:pk>/delete',views.AccessoryDelete.as_view(), name= 'accessory_delete'),
]