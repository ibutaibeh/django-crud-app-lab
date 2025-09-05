from django.shortcuts import render, redirect
from .models import Pokemon, Accessory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PurchaseForm
# Create your views here.
class PokemonCreate(CreateView):
    model=Pokemon
    fields=['name','type','power','weakness','image']

class PokemonUpdate(UpdateView):
    model=Pokemon
    fields=['name','type','power','weakness','image']

class PokemonDelete(DeleteView):
    model=Pokemon
    success_url='/pokemon/'

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def pokemon_index(request):
    pokemons= Pokemon.objects.all()
    return render(request,'pokemon/index.html',{'pokemons':pokemons})
def pokemon_details(request,pokemon_id):
    pokemon= Pokemon.objects.get(id=pokemon_id)
    purchase_form=PurchaseForm()
    return render(request,'pokemon/details.html',{'pokemon':pokemon, 'purchase_form':purchase_form})
def add_purchase(request,pokemon_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase=form.save(commit=False)
        new_purchase.pokemon_id=pokemon_id
        new_purchase.save()
        return redirect('details',pokemon_id=pokemon_id)


#Accessory CBVs views

class AccessoryList(ListView):
    model = Accessory
class AccessoryDetail(DetailView):
    model=Accessory
class AccessoryCreate(CreateView):
    model=Accessory
    fields= '__all__' # this means all field in the model (shortcut)

class AccessoryUpdate(UpdateView):
    model=Accessory
    fields='__all__'

class AccessoryDelete(DeleteView):
    model=Accessory
    success_url='/accessory/'
