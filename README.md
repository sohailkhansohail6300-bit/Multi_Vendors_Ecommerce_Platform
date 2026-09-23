# Multi-Vendor E-commerce Platform

A Django-based multi-vendor e-commerce application for managing products, customer accounts, seller profiles, and storefront functionality. The project follows a modular Django application structure with separate applications for accounts, products, and user profiles.

## Overview

The application provides a foundation for a marketplace where multiple vendors can manage product-related functionality while customers interact with the storefront and account system.

The project is currently configured for local development using Django and SQLite.

### Core Components

* **Products** — Product and storefront functionality.
* **Accounts** — Authentication and account-related views.
* **User Profiles** — Customer and seller profile functionality.
* **Django Admin** — Administrative interface for managing application data.
* **Media Handling** — Development media storage for uploaded files.
* **Templates** — Server-rendered HTML templates using the Django template engine.

## Technology Stack

* Python
* Django 6.0.1
* SQLite
* Django Templates
* HTML
* Pillow
* Django Mathfilters

Dependencies are defined in [`requirements.txt`](requirements.txt).

## Architecture

The project separates functionality into dedicated Django applications:

```text
Multi_Vendors_Ecommerce_Platform/
│
├── Accounts/
│   └── Account and authentication functionality
│
├── products/
│   └── Product and storefront functionality
│
├── userProfile/
│   └── User and seller profile functionality
│
├── confi/
│   └── Django project configuration
│
├── templates/
│   └── Shared HTML templates
│
├── media/
│   └── Uploaded development media
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

## Screenshots

### Storefront

<img width="1360" height="653" alt="image" src="https://github.com/user-attachments/assets/ddbd0080-7eb4-4a0d-80c0-31a5c13f8628" />
<img width="1360" height="688" alt="image" src="https://github.com/user-attachments/assets/389cd778-26b0-4214-ae07-edfcf5da17b5" /><img width="1354" height="654" alt="image" src="https://github.com/user-attachments/assets/2963eaa4-3d98-4fed-81c5-cd99342ebf2a" />
<img width="1355" height="654" alt="image" src="https://github.com/user-attachments/assets/7273024b-b86d-4ce8-8b80-16efe2077b37" />
<img width="1366" height="644" alt="image" src="https://github.com/user-attachments/assets/05b7f10f-73dd-4357-8f93-7505dd038b02" />
<img width="302" height="640" alt="image" src="https://github.com/user-attachments/assets/8afd9921-249f-4d55-8274-98985d0a88f9" />
<img width="1359" height="650" alt="image" src="https://github.com/user-attachments/assets/b599fc09-fe00-413a-8f5b-82a4bdbe9526" />





### Product Listing

<img width="1362" height="654" alt="image" src="https://github.com/user-attachments/assets/0c9d74b2-0d95-4b19-858c-36708a7f9e8e" />
<img width="1350" height="645" alt="image" src="https://github.com/user-attachments/assets/d6f1423f-86ca-42fa-b97b-b15426a1e059" />
<img width="301" height="642" alt="image" src="https://github.com/user-attachments/assets/364f92ea-532d-4b8b-80f2-10b0f987549f" />
<img width="292" height="642" alt="image" src="https://github.com/user-attachments/assets/70f901d3-1c58-45db-aa04-8fa8c579630c" />


### Product Details

<img width="1363" height="652" alt="image" src="https://github.com/user-attachments/assets/c8b18d84-4d43-462d-ae3a-1c845e760d67" />
<img width="1359" height="650" alt="image" src="https://github.com/user-attachments/assets/7b561558-ed9a-443f-85b0-23c3a846650d" />
<img width="287" height="631" alt="image" src="https://github.com/user-attachments/assets/64f0e7a8-f19c-462c-8f83-d4a6a4f59145" />
<img width="1358" height="653" alt="image" src="https://github.com/user-attachments/assets/9cfacfce-0cb7-401a-9126-3f2f00e72600" />
<img width="1357" height="648" alt="image" src="https://github.com/user-attachments/assets/753ec12f-e301-4e0c-a300-1768661c9838" />
<img width="1355" height="646" alt="image" src="https://github.com/user-attachments/assets/d8155440-91c9-4108-86a3-320b0f710d3f" />


### Seller Profile

<img width="1361" height="684" alt="image" src="https://github.com/user-attachments/assets/4d96221a-21ba-44d8-a55c-95a4963d29b9" />
<img width="305" height="631" alt="image" src="https://github.com/user-attachments/assets/6ffec37c-c725-411e-951f-bf6378029d72" />
<img width="291" height="650" alt="image" src="https://github.com/user-attachments/assets/8c512351-9f34-401d-9794-46ec8e1eb9da" />
<img width="1356" height="681" alt="image" src="https://github.com/user-attachments/assets/c97f494c-c670-46ca-bba5-57c9c4319d39" />
<img width="1358" height="696" alt="image" src="https://github.com/user-attachments/assets/31b9164e-00b1-4a61-a417-629b2bd6227b" />
<img width="1364" height="690" alt="image" src="https://github.com/user-attachments/assets/6e8f07a9-9403-43da-b5c4-390fe970207f" />



### Django Administration

<img width="1359" height="649" alt="image" src="https://github.com/user-attachments/assets/9c68de0a-1a26-44fc-a0ec-70697c3f8d80" />
<img width="1362" height="655" alt="image" src="https://github.com/user-attachments/assets/e8d8466d-3658-4a3e-b62e-92ed43e6ded5" />


## Requirements

* Python 3.10+
* pip
* Git
* Virtual environment

## Local Development

### Clone the repository

```bash
git clone https://github.com/sohailkhansohail6300-bit/Multi_Vendors_Ecommerce_Platform.git
cd Multi_Vendors_Ecommerce_Platform
```

### Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Start the development server

```bash
python manage.py runserver
```

Application:

```text
http://127.0.0.1:8000/
```

## Application Routes

| Route           | Purpose                       |
| --------------- | ----------------------------- |
| `/`             | Product storefront            |
| `/admin/`       | Django administration         |
| `/accounts/`    | Account-related functionality |
| `/userProfile/` | User profile functionality    |

## Database

The project currently uses SQLite for local development.

```text
Database: SQLite
File: db.sqlite3
```

For production environments, a production-grade relational database such as PostgreSQL should be considered.

## Media Files

Uploaded development files are stored under:

```text
media/
```

Media configuration should be reviewed before production deployment, particularly with regard to storage, access control, and serving uploaded files.

## Testing

Run the Django test suite with:

```bash
python manage.py test
```

## Production Considerations

The current configuration is intended for development. Before deploying the application to a production environment:

* Set `DEBUG = False`.
* Move `SECRET_KEY` to environment variables.
* Configure `ALLOWED_HOSTS`.
* Use a production database.
* Configure static file handling.
* Configure production media storage.
* Use a production WSGI/ASGI server.
* Review authentication and authorization configuration.
* Do not commit credentials or other sensitive configuration.
* Configure environment-specific settings.

## Project Status

This repository represents an actively developed Django e-commerce application. The current implementation focuses on the core application structure, product functionality, accounts, profiles, storefront pages, and administrative functionality.

Additional marketplace functionality can be implemented as the project evolves.

## Future Development

Potential areas for further development include:

* Order management
* Checkout workflow
* Payment integration
* Vendor dashboards
* Vendor-specific order management
* Inventory management
* Product search and filtering
* Product reviews and ratings
* Wishlist functionality
* Notifications
* Seller analytics
* Production deployment configuration

## License

No license has been specified for this repository.

## Repository

GitHub: [Multi_Vendors_Ecommerce_Platform](https://github.com/sohailkhansohail6300-bit/Multi_Vendors_Ecommerce_Platform?utm_source=chatgpt.com)

## Author

**Sohail Khan**

Python / Django Developer
