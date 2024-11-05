from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor, Inventory, Suggestion
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request, 'index.html')
def add_flavor(request):
    if request.method == 'POST':
        name = request.POST['name']
        seasonal = request.POST['seasonal']
        Flavor.objects.create(name=name, seasonal=seasonal)
        return redirect('view_flavors') 
    return render(request, 'add_flavor.html')


def view_flavors(request):
    flavors = Flavor.objects.all()
    return render(request, 'view_flavors.html', {'flavors': flavors})


def update_flavor(request, flavor_id):
    flavor = get_object_or_404(Flavor, id=flavor_id)
    if request.method == 'POST':
        flavor.name = request.POST['name']
        flavor.seasonal = request.POST['seasonal']
        flavor.save()  
        return redirect('view_flavors')  
    return render(request, 'update_flavor.html', {'flavor': flavor})


def delete_flavor(request, flavor_id):
    flavor = get_object_or_404(Flavor, id=flavor_id)
    flavor.delete()
    return redirect('view_flavors')  

def add_inventory(request):
    if request.method == 'POST':
        ingredient = request.POST['ingredient']
        quantity = request.POST['quantity']
        Inventory.objects.create(ingredient=ingredient, quantity=quantity)
        return redirect('view_inventory')  
    return render(request, 'add_inventory.html')

def view_inventory(request):
    inventory = Inventory.objects.all()
    return render(request, 'view_inventory.html', {'inventory': inventory})

def update_inventory(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        inventory_item.ingredient = request.POST['ingredient']  
        inventory_item.quantity = request.POST['quantity'] 
        inventory_item.save() 
        return redirect('view_inventory') 
    return render(request, 'update_inventory.html', {'inventory_item': inventory_item})

def delete_inventory(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, id=inventory_id)
    inventory_item.delete()
    return redirect('view_inventory')  

def add_suggestion(request):
    flavors = Flavor.objects.all()
    if request.method == 'POST':
        flavor_id = request.POST.get('flavor')
        if flavor_id == 'new_flavor':
            flavor_name = request.POST.get('new_flavor_name')
            if flavor_name:
                flavor = Flavor.objects.create(name=flavor_name)
                Suggestion.objects.create(flavor=flavor, allergies=request.POST['allergies'])
            else:
                return render(request, 'add_suggestion.html', {'flavors': flavors, 'error': 'New flavor name is required.'})
        elif flavor_id:  
            flavor = get_object_or_404(Flavor, id=flavor_id)
            Suggestion.objects.create(flavor=flavor, allergies=request.POST['allergies'])
        else:  
            return render(request, 'add_suggestion.html', {'flavors': flavors, 'error': 'Flavor is required.'})
        return redirect('view_suggestions')
    return render(request, 'add_suggestion.html', {'flavors': flavors})

def view_suggestions(request):
    suggestions = Suggestion.objects.all()
    return render(request, 'view_suggestions.html', {'suggestions': suggestions})

def delete_suggestion(request, suggestion_id):
    """Delete a suggestion."""
    suggestion = get_object_or_404(Suggestion, id=suggestion_id)
    suggestion.delete()
    return redirect('view_suggestions') 