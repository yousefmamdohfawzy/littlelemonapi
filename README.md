# Little Lemon API Documentation

## Overview

The Little Lemon API is a Django REST framework-based project providing robust endpoints for managing a restaurant's operations. The API supports user management, menu item management, cart operations, and order processing with role-based permissions (Customer, Delivery Crew, Manager, and Admin).

-------------------------------------------------

## Installation and Setup
#### Prerequisites:
1- Python 3.9+

2- Django 5.1+

3- Django REST Framework

4- PostgreSQL (optional, based on your configuration)

<br>

**Steps to Setup :**

1- Clone the repository:
``` bash
    git clone <https://github.com/yousefmamdohfawzy/littlelemon_api.git>
    cd LittleLemon
```

2- Install dependencies:
``` bash
    pip install -r requirements.txt
```

3- Run migrations:
``` bash
    python manage.py migrate
```

4- Create a superuser for admin access:
``` bash
    python manage.py createsuperuser
```

5- Start the development server:
``` bash
    python manage.py runserver
```

------------------------------------------
**API Endpoints**

Authentication and User Management


| Endpoint                         | Method | Role  | Description                     |
|----------------------------------|--------|-------|---------------------------------|
| `/api/users/<id>/groups/`          | POST   | Admin | Assign a user to a group        |
| `/api/users/<id>/groups/ `        | DELETE | Admin | Remove a user from a group      |
| `/api/groups/manager/users/`       | GET    | Admin | List all managers               |
| `/api/groups/delivery-crew/users/` | GET    | Admin | List all delivery crew members  |

----------------------------------------------------------

Menu Management

| Endpoint                | Method        | Role     | Description                  |
|-------------------------|---------------|----------|------------------------------|
| `/api/menu-items/`      | GET           | Public   | List all menu items.         |
| `/api/menu-items/`      | POST          | Manager  | Add a new menu item.         |
| `/api/menu-items/<id>/` | GET           | Public   | Retrieve a menu item by ID.  |
| `/api/menu-items/<id>/` | PUT, DELETE   | Manager  | Update or delete a menu item.|
Features:
Filtering and Sorting: Filter by title, price, category, or featured status.
```bash
GET /api/menu-items/?category=Beverages&ordering=-price
```
 ----------------------------------------------------------

Cart Operations

| Endpoint                                   | Method | Role      | Description                  |
|-------------------------------------------|--------|-----------|------------------------------|
| `/api/users/<id>/cart/menu-item/<menu_id>/`   | POST   | Customer  | Add a menu item to the cart. |
| `/api/users/<id>/cart/menu-item/`             | GET    | Customer  | View all items in the cart.  |
| `/api/users/<id>/cart/`                       | DELETE | Customer  | Clear all items in the cart. |


----------------------------------------------------------

Order Management

| Endpoint         | Method         | Role                 | Description                  |
|------------------|---------------|----------------------|------------------------------|
| `/api/orders/`   | GET, POST      | Customer             | Place an order or view orders. |
| `/api/orders/<id>/` | GET, PUT, DELETE | Customer, Manager, Delivery Crew | Manage a specific order.       |

#### Order Status
- 0: Delivery in Progress
- 1: Delivered

#### Role-Specific Actions
- Customer: Place orders, view their orders.
- Manager: View all orders, assign delivery crew.
- Delivery Crew: View assigned orders, update status.

--------------------------

### Models Overview
- Category: Represents menu categories.
- MenuItem: Represents individual menu items.
- Cart: Tracks menu items added by a customer.
- Order: Represents an order placed by a customer.
- OrderItem: Items included in an order.

-------------------------------

 **Permissions**

| Role            | Access Description                                      |
|------------------|--------------------------------------------------------|
| **Public**       | Can view menu items.                                   |
| **Customer**     | Can manage their cart, place orders, and view their orders. |
| **Manager**      | Can manage menu items and assign orders to delivery crew. |
| **Delivery Crew**| Can view assigned orders and update their status.      |
| **Admin**        | Can manage users and groups.                           |

------------------------
**HTTP Status Codes**
| Code | Description                              |
|------|------------------------------------------|
| 200  | Successful operation.                    |
| 201  | Resource created successfully.           |
| 400  | Bad request.                             |
| 401  | Authentication required.                 |
| 403  | Forbidden. Insufficient permissions.     |
| 404  | Resource not found.                      |
| 500  | Internal server error.                   |
----------------------------
### Throttling
- Authenticated Users: 20 requests/minute
- Anonymous Users: 10 requests/minute
-------------------------
### Admin Features
- View and manage menu items, categories, users, orders, and carts via the admin panel.