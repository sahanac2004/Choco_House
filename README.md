# Choco_House
# Chocolate House Application

This is a simple Django application for managing a fictional chocolate house. The application allows users to manage seasonal flavor offerings, ingredient inventory, and customer flavor suggestions with allergy concerns. The data is managed using SQLite.

## Features

- Add, view, update, and delete seasonal flavors.
- Add, view, update, and delete ingredient inventory.
- Add, view, and delete customer flavor suggestions along with allergy concerns.

## Requirements

- Python 3.x
- Django 3.x or higher
- SQLite (default with Django)
- Docker (for containerization, optional)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sahanac2004/Choco_House.git
   cd Choco_House
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

##Docker Setup
This application can also be run in a Docker container. Follow these steps to set it up:

1. Build the Docker image:

docker build -t chocolate-house-app .

2.Run the Docker container:

docker run -p 8000:8000 chocolate-house-app

3.Access the application:

Open your web browser and go to http://127.0.0.1:8000/.

##Testing the Application
To validate the application, you can follow these steps:

1. Add Seasonal Flavors:

Navigate to /flavors/add/ to add a new flavor.
Ensure that the flavor appears in the /flavors/ list after adding.

2. Update Seasonal Flavors:

Click on the update link next to a flavor in the /flavors/ list.
Change the flavor details and save.
Verify the changes are reflected in the list.

3.Delete Seasonal Flavors:

Click on the delete link next to a flavor in the /flavors/ list.
Confirm the deletion and ensure the flavor is no longer listed.

4.Manage Ingredient Inventory:

Navigate to /inventory/add/ to add an ingredient.
Check the inventory list at /inventory/ to ensure it has been added.

5.Add Flavor Suggestions:

Go to /suggestions/add/ to submit a flavor suggestion.
Ensure the suggestion appears in the /suggestions/ list.

6.Handle Edge Cases:

Try adding a suggestion without selecting a flavor or entering a new flavor name to validate error handling.
Attempt to delete a flavor or inventory item that does not exist to ensure proper error handling.

##Code Documentation
The code is structured into views.py, urls.py, and models.py files.
Each function in views.py is documented with comments explaining its purpose and behavior.
Models in models.py define the database schema for flavors, inventory, and suggestions.

##Edge Cases Handled
Flavor suggestions require a selected flavor or a new flavor name.
Updating and deleting operations check for the existence of the object before proceeding.
Error messages are displayed when required fields are not filled.

##Acknowledgements
Django documentation for guidance on building web applications.
SQLite documentation for database management.

## requirements.txt and Dockerfile
Instructions for Use
1.Create the Files:

Create a new file named requirements.txt in the root of your project and copy the contents provided above.
Create a new file named Dockerfile in the root of your project and copy the contents provided above.

2.Add Additional Dependencies: If your application uses any other libraries (like Django REST framework, etc.), make sure to list them in the requirements.txt file.

3.Building the Docker Image: Once you have these files in place, you can build your Docker image using the command:

docker build -t chocolate-house-app .

4.Running the Docker Container: After building the image, you can run it using:

docker run -p 8000:8000 chocolate-house-app
This setup will provide you with a Docker container running your Django application, accessible at http://127.0.0.1:8000/
