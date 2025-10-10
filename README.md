# Authentication App

🎉 Live In-production Web-link: https://dev-accounts-qwaz.onrender.com

# User Authentication and Profile Management App
- ✅ Basic email-based signup and login 
- ✅ Basic password requirements 
- ✅ Account deletion 
- ✅ Update email 
- ✅ Custom 404 (Credit at bottom)  

## Development Plan:
- ✅ Use PostgreSQL in Production server 
- ✅  Deploy on Render.com under free-instance 
- 🏗️ Connect DataDog for app analytics
- 🏗️ Connect email backend provider
- Setup email - password reset with expiring links
- Setup email - verification on accounts upon setup with expiring links 
- Setup OAuth (ie. Google, Github account login ability)
- Configure MFA/2FA with a SMS service such as Twilio with existing plan
- Add enhanced security with account lockouts and rate limiting on 
password attempts
- Improved cookie and session management 
- Captcha before login 
- May consider magic link login and look for IP geolocation anomalies.


## Overview

This project demonstrates a basic authentication workflow in Django:
- User registration (signup)
- Login and logout
- Profile page with email update and account deletion
- Password reset using Django's built-in tools is currently deactivated (non-active) in development but maybe activated in production.
- Custom animated 404 error page 

---

## Requirements

- Python 3.10 or higher  
- Django 5.x  
- PostgreSQL (recommended for production) or SQLite (default)

See `requirements.txt` for a full list of dependencies.

---



## Setup Instructions

1. Clone the repository:
 
git clone https://github.com/pshunt/dev-accounts
cd dev-accounts


2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate

5. Start the development server:

python manage.py runserver

6. Visit the app in your browser:

    http://127.0.0.1:8000

URLs

Function		URL
Signup			/accounts/signup/
Login			/accounts/login/
Profile			/profile/
Password Reset	/accounts/password_reset/ (non-active)
Home			/
Custom 404		Visit a non-existent route


Folder Structure 
Note: To view properly, please click and view under "Raw" setting

project_root/
├── core/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── templates/core/
│       └── profile.html
│
├── templates/
│   ├── 404.html
│   └── registration/
│       ├── login.html
│       ├── signup.html
│       └── password_reset_form.html
│
├── static/
│   ├── css/
│   │   ├── styles.css
│   │   └── 404.css
│   ├── js/
│   │   └── 404.js
│   └── media/
│       ├── demo1.mp4
│       ├── demo2.mp4
│       ├── demo3.mp4
│       ├── demo4.mp4
│       └── demo5.mp4
│
├── manage.py
├── requirements.txt
└── README.md

<h3>Instructional Videos</h3>

# Sign-up Process
https://github.com/user-attachments/assets/eb983dc6-3624-426c-acaa-847e7559a9d8

# Updating Email on Profile Page
https://github.com/user-attachments/assets/280f00e1-4a62-4b05-832c-708515985701

# Deleting an Account on Profile Page 
https://github.com/user-attachments/assets/2867eba7-ea24-45ec-93c3-a5436db62cc4

# Redirecing to Login or Profile Page Based on Status
https://github.com/user-attachments/assets/a5065fb6-1cea-4045-a949-78a71a913a26

# 404 Example if Landing on a Malformed-link Page
https://github.com/user-attachments/assets/56144f70-777b-4945-aa1a-70f993cea427


Additiional Notes

    Use SQLite for local testing and PostgreSQL for deployment.

    To change databases, update the DATABASES setting in project_root/settings.py.

    Run python manage.py createsuperuser to access the Django admin panel.

Aknowledgements:

Custom 404 page and code was designed and written by Ahmed B. Hameed:
https://codepen.io/Ahmed_B_Hameed/pen/LZqNmp