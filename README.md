Vendor Management System using Django and Django REST Framework
This project implements a Vendor Management System with features for managing vendor profiles, tracking purchase orders, and calculating vendor performance metrics.

Features
Vendor Profile Management:
Create, retrieve, update, and delete vendors via REST API.
Purchase Order Tracking:
Manage purchase orders, including creation, retrieval, updating, and deletion.
Vendor Performance Evaluation:
Track performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Setup Instructions
To set up the project locally, follow these steps:

Prerequisites
Python 3.x
Django
Django REST Framework
Virtual environment (recommended)
Installation
PostgreSQL

Clone the repository:

```bash

git clone https://github.com/yourusername/vendor-management-system.git
```
cd vendor-management-system

Set up a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install dependencies:
```
pip install -r requirements.txt
```

Update the database configurations in VMS/settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
Create a superuser (for admin access):

python manage.py createsuperuser

```

Start the development server:
```
python manage.py runserver
```
Access the API endpoints locally at http://localhost:8000/api/

## API Endpoints

Vendors

POST /api/vendors/
Create a new vendor.

GET /api/vendors/
List all vendors.

GET /api/vendors/{vendor_id}/
Retrieve details of a specific vendor.

PUT /api/vendors/{vendor_id}/
Update details of a specific vendor.

DELETE /api/vendors/{vendor_id}/
Delete a specific vendor.

Purchase Orders
POST /api/purchase_orders/
Create a new purchase order.

GET /api/purchase_orders/
List all purchase orders.

GET /api/purchase_orders/{po_id}/
Retrieve details of a specific purchase order.

PUT /api/purchase_orders/{po_id}/
Update details of a specific purchase order.

DELETE /api/purchase_orders/{po_id}/
Delete a specific purchase order.

Vendor Performance
GET /api/vendors/{vendor_id}/performance/
Retrieve performance metrics for a specific vendor.


## Authentication
API endpoints are secured with token-based authentication. create a tocken with superuser credentials and use it to get a tocken 
