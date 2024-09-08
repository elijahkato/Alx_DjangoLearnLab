# Alx_DjangoLearnLab
On to new Things Called Django

# Bookshelf Application

## Overview

The `bookshelf` app is a Django application that manages books with detailed access control using custom permissions and groups. The app includes models, views, and templates that utilize Django's built-in authentication and permission systems to restrict access based on user roles.

## Custom Permissions and Groups

### Book Model

The `Book` model is defined in `models.py` and includes the following custom permissions:

- **`can_view`**: Allows users to view book listings.
- **`can_create`**: Allows users to create new books.
- **`can_edit`**: Allows users to edit existing books.
- **`can_delete`**: Allows users to delete books.



# Custom Views for Book Model in Django REST Framework

## Overview
This API handles CRUD operations for the Book model using Django REST Framework's generic views. Each endpoint is designed to handle specific operations, such as listing books, retrieving details, creating new entries, updating existing records, and deleting entries.

## Endpoints
- **GET /books/**: List all books. Open to all users.
- **GET /books/<id>/**: Retrieve details of a specific book by ID. Open to all users.
- **POST /books/create/**: Create a new book. Restricted to authenticated users.
- **PUT /books/<id>/update/**: Update an existing book. Restricted to authenticated users.
- **DELETE /books/<id>/delete/**: Delete a book. Restricted to authenticated users.

## Customizations
- CreateView and UpdateView include custom logic for data validation and handling special requirements.
- Permission classes are applied to ensure that only authenticated users can modify data, while read-only access is open to everyone.

## Testing
Use Postman or curl to manually test each endpoint. Confirm that permissions are enforced and that the views behave as expected.
