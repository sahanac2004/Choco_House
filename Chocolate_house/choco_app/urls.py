from django.urls import path
from django.urls import path
from .views import (
    index,
    add_flavor,
    view_flavors,
    update_flavor,
    delete_flavor,
    add_inventory,
    view_inventory,
    update_inventory,
    delete_inventory,
    add_suggestion,
    view_suggestions,
    delete_suggestion
)

urlpatterns = [
    path('', index, name='index'),
    path('flavors/add/', add_flavor, name='add_flavor'),
    path('flavors/', view_flavors, name='view_flavors'),
    path('flavors/update/<int:flavor_id>/', update_flavor, name='update_flavor'),
    path('flavors/delete/<int:flavor_id>/', delete_flavor, name='delete_flavor'),
    path('inventory/add/', add_inventory, name='add_inventory'),
    path('inventory/', view_inventory, name='view_inventory'),
    path('inventory/update/<int:inventory_id>/', update_inventory, name='update_inventory'),
    path('inventory/delete/<int:inventory_id>/', delete_inventory, name='delete_inventory'),
    path('suggestions/add/', add_suggestion, name='add_suggestion'),
    path('suggestions/', view_suggestions, name='view_suggestions'),
    path('suggestions/delete/<int:suggestion_id>/', delete_suggestion, name='delete_suggestion'),
]