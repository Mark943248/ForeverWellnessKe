## Project Overview
ForeverWellness is a web platform designed to showcase and sell Forever Living products. The goal is to provide a seamless shopping experience for users looking for natural health supplements, weight management tools, and skincare products.

## Key Features
Product Catalog: Organized categories (Nutrition, Bee Products, etc.).

Detailed Product Pages: product images, descriptions, and ingredient lists.

Search & Filter: Quickly find products by name or health benefit.

Responsive Design: Fully optimized for mobile, tablet, and desktop users.

Contact/Inquiry Form: Direct line for customers to ask about specific health regimens.

## Built With
Frontend: HTML/CSS,JS
Backend: Django      

## Overview

This is the Forever Wellness Django application. It uses Docker and PostgreSQL for development, and Cloudinary for media storage and image uploads.

## What this guide covers

- Docker setup on another developer machine
- Required environment variables
- Cloudinary setup reminder
- Starting the app locally
- Creating a Django superuser for admin access
- Posting products and blog entries through the admin page

## Prerequisites

- Docker installed and running
- Docker Compose available
- A Cloudinary account
- Git clone of this repository

## Recommended folder structure

The project repository root contains:

- `Dockerfile`
- `requirements.txt`
- `foreverwellness/docker-compose.yaml`
- `foreverwellness/manage.py`
- Django apps: `Blog`, `Pages`, `Products`

## Cloudinary setup

This project uses Cloudinary for media uploads and CKEditor file storage.

1. Sign up at https://cloudinary.com/
2. Create a new Cloudinary application
3. Copy the following credentials:
   - `CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`

> Reminder: You must set Cloudinary values in the `.env` file before starting the app, otherwise image uploads and admin media storage will fail.

## Environment variables

Create a `.env` file in the `foreverwellness` folder (next to `docker-compose.yaml`). The project loads environment variables from this file.

Example `.env` values:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=foreverwellness
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

CLOUD_NAME=your-cloudinary-cloud-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret
```

> Note: `DB_HOST` should be `db` for Docker Compose because the PostgreSQL service is named `db`.

## Start the app with Docker Compose

From the `foreverwellness` folder, run:

```bash
docker compose up --build
```

This will start two containers:

- `foreverwellness_web` for the Django app
- `foreverwellness_db` for PostgreSQL

Once started, the website is available at:

```text
http://localhost:8000
```

## Run migrations and create a superuser

If you need to run commands inside the web container, use:

```bash
docker exec -ti foreverwellness_web python manage.py migrate

docker exec -ti foreverwellness_web python manage.py createsuperuser
```

Follow the prompts to create the first admin user.

## Accessing the Django admin page

Open the admin page in your browser:

```text
http://localhost:8000/FWKE-dashboard/
```

Sign in with the superuser credentials created previously.

## Two-factor authentication (OTP)

This project uses Django Two-Factor Authentication for admin access.

- After entering your username and password
- If you wish to activate django-otp visit 
http://localhost:8000/account/two_factor/setup/
- If using an authenticator app e.g Google Authenticator, scan the QR code and enter the generated code.
-Generate and save backup codes in a safe place so you can sign in if your phone is unavailable.

If you are already logged out or want to reset OTP setup, log in again and follow the prompts on the two-factor page.

## Posting products and blogs

Product and blog content are managed through the Django admin interface.

1. Log in at `http://localhost:8000/FWKE-dashboard/`
2. Use the `Products` section to add or edit products
3. Use the `Blog` section to add or edit blog posts

Notes:

- Blog and product images are stored via Cloudinary.
- The admin interface uses CKEditor for rich text editing.
- Make sure Cloudinary credentials are correctly set before uploading images.

## Optional local Python environment

If you want to run without Docker, you can use a Python virtual environment.

From the repository root:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Then set the same environment variables locally and run:

```bash
cd foreverwellness
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000`.

## Troubleshooting

- If admin login is blocked, check `axes` lockout settings and reset failed login counts if needed.
or run 
`docker exec -ti foreverwellness_web python manage.py axes_reset`
- If image uploads fail, verify Cloudinary API keys and account status.
- If the database does not connect, confirm `.env` values and Docker Compose service status.

## Summary

1. Set up Cloudinary and save credentials
2. Create `.env` in `foreverwellness`
3. Run `docker compose up --build`
4. Run migrations and create superuser
5. Add products and blog posts via admin
