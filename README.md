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
