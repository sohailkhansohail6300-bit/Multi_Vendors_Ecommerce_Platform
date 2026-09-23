# Multi-Vendor E-commerce Platform

A Django-based multi-vendor e-commerce platform for managing products, customer accounts, seller profiles, and user-facing storefront pages.

## Overview

This project is built with Django and uses SQLite for local development. The application is organized into separate Django apps for products, accounts, and user profiles.

### Main components

- **Products** — storefront and product-management functionality.
- **Accounts** — account-related views and authentication routes.
- **User profiles** — profile and seller-related functionality.
- **Django admin** — administrative access at `/admin/`.
- **Media uploads** — development media files are served from the `media/` directory.

## Technology stack

- Python
- Django 6.0.1
- SQLite
- Django Mathfilters
- HTML templates
- Pillow

The complete dependency list is available in [`requirements.txt`](requirements.txt).

## Project structure

```text
.
├── Accounts/        # Account application
├── confi/            # Django project configuration
├── media/            # Uploaded media files
├── products/         # Product and storefront application
├── templates/        # Shared HTML templates
├── userProfile/      # User profile application
├── db.sqlite3        # Local SQLite database
├── manage.py         # Django management script
└── requirements.txt  # Python dependencies
```

## Requirements

- Python 3.10 or later
- `pip`
- A virtual environment is recommended

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sohailkhansohail6300-bit/Multi_Vendors_Ecommerce_Platform.git
   cd Multi_Vendors_Ecommerce_Platform
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell:**

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Optionally create an administrator account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Important URLs

- `/` — product storefront
- `/admin/` — Django administration
- `/accounts/` — account-related pages
- `/userProfile/` — user profile pages

## Development notes

The project currently uses SQLite and Django's development configuration. Before deploying to production:

- Move `SECRET_KEY` to an environment variable.
- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS`.
- Use a production-ready database and web server.
- Configure static and media file storage securely.
- Do not commit private credentials or sensitive production data.

## Running tests

Run the Django test suite with:

```bash
python manage.py test
```

## License

No license has been specified for this project yet.
