from django.shortcuts import render
from .models import Pokemon
# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def pokemon_index(request):
    pokemons= Pokemon.objects.all()
    return render(request,'pokemon/index.html',{'pokemons':pokemons})
def pokemon_details(request,pokemon_id):
    pokemon= Pokemon.objects.get(id=pokemon_id)
    return render(request,'pokemon/details.html',{'pokemon':pokemon})