# Little Lemon API Documentation

## Overview


The Little Lemon API is a Django REST Framework-based backend system designed to streamline restaurant operations. It provides endpoints for managing user roles, menu items, orders, and carts. This API ensures secure role-based access for Customers, Delivery Crew, Managers, and Admins, supporting essential features such as authentication, filtering, sorting, and throttling.




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
    git clone <https://github.com/yousefmamdohfawzy/littlelemonapi.git>
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

### **Authentication and User Management**


| Endpoint                         | Method | Role  | Description                     |
|----------------------------------|--------|-------|---------------------------------|
| `/api/users`          | POST   | Public  | Register a new user.                 |
| `/api/users/me`       | GET    | Any Authenticated User | Get details of the current user. |
| `/api/users/<id>/groups/`          | POST   | Admin | Assign a user to a group        |
| `/api/users/<id>/groups/ `        | DELETE | Admin | Remove a user from a group      |
| `/api/groups/manager/users/`       | GET    | Admin | List all managers               |
| `/api/groups/delivery-crew/users/` | GET    | Admin | List all delivery crew members  |
| `/auth/token/login/  ` | POST | Admin | Generate Token by usernaem and password | 

----------------------------------------------------------
### **Category Endpoints**
| Endpoint              | Method | Role    | Description                  |
|-----------------------|--------|---------|------------------------------|
| `/api/categories`     | GET    | Public  | List all categories.         |
| `api/categories/`     |  POST  | Admin   | Add a new category           |
| `api/categories/`     | DELETE | Admin   | Remove a category            |

-----------

### **Menu Management**

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

### **Cart Operations**

| Endpoint                                  | Method |  Role     |   Description                |
|-------------------------------------------|--------|-----------|------------------------------|
| `/api/users/carts/menu-item/<menu_id>/`   | POST   | Customer  | Add a menu item to the cart. |
| `/api/users/carts/me/`                    | GET    | Customer  | View all items in the cart.  |
| `/api/users/carts/me/`                    | DELETE | Customer  | Clear all items in the cart. |


----------------------------------------------------------

### **Order Management**

| Endpoint              | Method            | Role                          | Description                  |
|------------------     |---------------    |----------------------         |------------------------------|
| `/api/orders/`        | GET, POST         | Customer                      |Place an order or view orders |
| `/api/orders/<id>/`   | GET, PUT, DELETE  |Customer,manager,delivery-crew | Manage a specific order.    |

#### Order Status
- 0: Delivery in Progress
- 1: Delivered

#### Role-Specific Actions
- Customer: Place orders, view their orders.
- Manager: View all orders, assign delivery crew.
- Delivery Crew: View assigned orders, update status.

--------------------------
## **Models Overview**

### **Category**
- **Fields:**
  - `slug`: Unique identifier for the category.
  - `title`: Unique, descriptive title.
  
### **MenuItem**
- **Fields:**
  - `title`: Name of the menu item.
  - `price`: Cost of the item.
  - `featured`: Boolean to highlight items.
  - `category`: ForeignKey to Category.

### **Cart**
- **Fields:**
  - `user`: Associated user.
  - `menuitem`: Associated menu item.
  - `quantity`: Quantity added.
  - `unit_price`: Price per unit.
  - `price`: Total price.

### **Order**
- **Fields:**
  - `user`: Customer placing the order.
  - `delivery_crew`: Assigned delivery crew.
  - `status`: Boolean for delivery status.
  - `items`: Related `OrderItem` objects.

### **OrderItem**
- **Fields:**
  - `order`: Associated order.
  - `menuitem`: Menu item in the order.
  - `quantity`: Number of units.
  - `unit_price`: Price per unit.
  - `price`: Total price.


--------------
### **Permissions**

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

--------------------------------

### Pre-Configured Users

The following users are pre-configured for testing purposes:

| Username   | Email             | Role          | Password |  User     |                Token                    |
|------------|-------------------|---------------|----------|-----------|-------------------------------------|
| manager    | manager@mail.com  | Manager       | 123      | superuser |f9e4e35ec3ccec3d866b1bccc9dd1c3c8661c2a1 |
| manager2   | manager2@mail.com | Manager       | 123      | superuser |eb5c7009277d6be01b64da2b0fd60d895629cdf7 |
| delivery   | delivery@mail.com | Delivery Crew | 123      | staffuser |
| delivery2  | d@d.com           | Delivery Crew | 123      | staffuser |
| customer   | c@c.co            | Customer      | 123      |   user    |

**Note**:
- Password validation rules were bypassed for testing purposes.
- Update these credentials and implement stricter password policies for production environments.<br><br>


**Command for Superuser Creation:**
```bash
python manage.py createsuperuser
```
---------------------------------

### Installed Dependencies

The project uses the following dependencies:

| Dependency                               | Version  |
|------------------------------------------|----------|
| Django                                   | 5.1.2    |
| djangorestframework                      | 3.15.2   |
| djangorestframework-simplejwt            | 5.3.1    |
| djoser                                   | 2.2.3    |
| social-auth-app-django                   | 5.4.2    |
| cryptography                             | 43.0.3   |
| python3-openid                           | 3.2.0    |

**Install Dependencies**:
Run the following command to install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```


Contributors
Yousef Fawzy: Backend Developer
For further queries, contact: youseffawzy249@gmail.com
linkedin : https://www.linkedin.com/in/yousefmamdohfawzy/