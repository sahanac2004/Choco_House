# Chocolate House Application

This is a simple Django application for managing a fictional chocolate house. The application allows users to manage seasonal flavor offerings, ingredient inventory, and customer flavor suggestions with allergy concerns. The data is managed using SQLite.

## Problem Statement
Create a simple Python application for a fictional chocolate house that uses SQLite to manage:

1. Seasonal flavor offerings
2. Ingredient inventory
3. Customer flavor suggestions and allergy concerns

## Features

- **Flavor Management:** Add, view, update, and delete seasonal flavors.
- **Inventory Management:** Add, view, update, and delete ingredient inventory.
- **Customer Suggestions:** Add, view, and delete customer flavor suggestions, including any allergy information.

## Requirements or Tech Stack

- Python 3.x
- Django 3.x or higher
- SQLite (default with Django)
- Docker (for containerization, optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sahanac2004/Choco_House.git
cd Choco_House
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Run database migrations:
```bash
python manage.py migrate
```
5.Create a superuser (optional for admin access):
```bash
python manage.py createsuperuser
```
6. Run the development server:
```bash
python manage.py runserver
```
7. Open your browser and navigate to http://127.0.0.1:8000/.


# Docker Setup (Optional)
This application can also be run in a Docker container. Follow these steps to set it up:

1. Build the Docker image:
```bash
docker build -t chocolate-house-app .
```
2.Run the Docker container:
```bash
docker run -p 8000:8000 chocolate-house-app
```
3.Access the application:

Open your web browser and go to http://127.0.0.1:8000/.

# Testing the Application
To validate the application, you can follow these steps:
**Features**
This Chocolate House Application provides a variety of features to manage seasonal flavors, ingredient inventory, and customer flavor suggestions. Below are the details for each section accessible from the homepage:

**1. Flavor Management**
1. Add Flavor: Allows users to add a new flavor by specifying its name and seasonal category. Options include "Spring," "Summer," "Autumn," "Winter," and "No season."

  -- URL: /flavors/add/
  -- Form Fields:
       -- Flavor Name: Text input for the name of the flavor.
       -- Select Seasonal Category: Dropdown to choose the seasonal category.
2. View Flavors: Displays a list of all seasonal flavors with options to update or delete each flavor entry.
    
  - URL: /flavors/
  - Table Columns:
       - Flavor: Displays the flavor name.
       - Seasonal: Shows the seasonal category of each flavor.
       - Actions: Links to "Edit" and "Delete" each flavor.
3. Update Flavor: Provides a form to edit a flavor's name and seasonal category.

  - URL: /flavors/update/<id>/
  - Form Fields:
       - Flavor Name: Prefilled with the current flavor name.
       - Select Seasonal Category: Dropdown to update the seasonal category.
**2. Ingredient Inventory Management**
1. Add Inventory: Allows users to add new ingredients to the inventory, including the ingredient name and quantity.

   - URL: /inventory/add/
   - Form Fields:
       -  Ingredient: Text input for the name of the ingredient.
       -  Quantity: Numeric input for the quantity available.
2. View Inventory: Lists all ingredients with their quantities and provides options to update or delete each item.

  - URL: /inventory/
  - Table Columns:
       -  Ingredient: The name of each ingredient.
       -  Quantity: The current quantity in stock.
       -  Actions: Links to "Edit" and "Delete" each inventory item.
3. Update Inventory Item: Allows users to edit the ingredient name and quantity.

  - URL: /inventory/update/<id>/
  - Form Fields:
        - Ingredient: Prefilled with the ingredient's name.
        - Quantity: Prefilled with the current quantity.
**3. Customer Flavor Suggestions**
1. Add Suggestion: Enables customers to submit flavor suggestions, either by selecting an existing flavor or suggesting a new flavor. Users can also specify any allergy concerns associated with the suggestion.

  - URL: /suggestions/add/
  - Form Fields:
        - Flavor: Dropdown to select an existing flavor or add a new flavor.
        - New Flavor Name: Text input for entering a new flavor name (only visible if "Suggest New Flavor" is selected).
        -  Allergies: Text area to describe any allergy concerns.
2. View Suggestions: Lists all customer flavor suggestions, showing the suggested flavor and any associated allergies. Users can delete suggestions from this view.

  - URL: /suggestions/
  - Table Columns:
        - Flavor: The suggested flavor's name.
        - Allergies: Allergy information provided by the customer.
        - Actions: Link to delete each suggestion.
Each of these features is accessible from links on the homepage (index.html) under the following options:

- Add Flavor
- View Flavors
- Add Inventory
- View Inventory
- Add Suggestion
- View Suggestions

# Code Documentation
The code is structured into views.py, urls.py, and models.py files.
- views.py: Contains functions for each view in the application, each documented with comments explaining their purpose.
- models.py: Defines the database schema, with models for flavors, inventory, and suggestions.

# Edge Cases Handled
- Flavor Suggestions: Users must select an existing flavor or enter a new flavor name when submitting suggestions.
- Update/Delete Operations: Checks for the existence of an object before allowing updates or deletions.
- Error Handling: Displays error messages if required fields are missing.

# Acknowledgements
Django documentation for guidance on building web applications.
SQLite documentation for database management.

# requirements.txt and Dockerfile
Instructions for Use

1.Add Additional Dependencies: If your application uses any other libraries (like Django REST framework, etc.), make sure to list them in the requirements.txt file.

2.Building the Docker Image: Once you have these files in place, you can build your Docker image using the command:
```bash
docker build -t chocolate-house-app .
```
3.Running the Docker Container: After building the image, you can run it using:
```bash
docker run -p 8000:8000 chocolate-house-app
```
This setup will provide you with a Docker container running your Django application, accessible at http://127.0.0.1:8000/
**Contact**
For questions or suggestions, please contact sahanac629@gmail.com.
