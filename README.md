# Django_Blogging_Website
# Glasgow Life

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#database-setup)
  - [Create an Admin User](#create-an-admin-user)
  - [Running the Development Server](#running-the-development-server)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Glasgow Life - A Campus Information Sharing Platform is a Django-based website created as part of the MSc Software Development Course. It serves as an online platform for students and teachers to exchange information related to campus life. Users can post and browse various campus-related information, including courses, events, announcements, discussions, and more. The platform's primary goal is to foster an efficient, user-friendly, and enjoyable online campus community.

## Features

- **Real-time Updates**: The platform provides real-time updates on campus news and events, ensuring that users stay informed about the latest happenings.

- **Information Variety**: Users can share a wide range of campus-related information, making it a versatile platform for communication and knowledge exchange.

- **Administrator Review**: To maintain information quality and safety, the platform includes an administrator review function. This feature verifies, filters, and manages the information posted on the platform, ensuring the accuracy and authenticity of the content.

## Getting Started

Follow these steps to set up and run the Campus Information Sharing Platform on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

```bash

### Set Up a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

#### Install Dependencies:
pip install -r requirements.txt

```

### Database Setup
Migrate Database:
```bash
python manage.py migrate
```

### Create an Admin User
To access the admin panel and manage the website, create an admin user:

```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### Running the Development Server
Start the development server:

``` bash
python manage.py runserver
```
The website should now be accessible at http://localhost:8000 in your web browser.

### Deployment
To deploy this website to a production environment, please follow the deployment guidelines for Django projects. Make sure to configure your server, database, and static files correctly. Don't forget to update the DEBUG setting in your settings.py to False for production.

## It has been deployed at http://glasgowlife.pythonanywhere.com/

### Contributing
We welcome contributions to enhance and improve the Campus Information Sharing Platform. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License.

### Acknowledgments
The creators and maintainers of Django for providing a robust web framework.
