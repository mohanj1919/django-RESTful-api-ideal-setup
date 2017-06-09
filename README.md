ideal-setup

Following the Django setup from following series of blog posts. https://medium.com/@djstein/modern-django-part-0-introduction-and-initial-setup-657df48f08f8 

* https://tests4geeks.com/django-rest-framework-tutorial/

* command to create virtual env
python3 -m venv <venv_name>

* migrate tables command
python manage.py migrate --settings=config.settings.local

* run server command
python manage.py runserver --settings=config.settings.local

# Roles:

- Admin
- User (curator)

# Admin Screens
- Login (2 screens as we are implementing two factor auth)
- Forgot Password
- Add new Curator/Admin
- Edit Curator/Admin
- Create Template
- Edit Template
- Create Cohort (Includes following functionalities)
  - Add/Upload Patients
  - Assign Curators
  - Add Templates
- Dashboard/QuickView
  - View by Curator
  - View by Cohort
  - View by Template

# User (curator) Screens
- Login (2 screens as we are implementing two factor auth)
- Forgot Password
- Landing page (which shows assigned project)
- Search page (search by template)
- Chart Review ([Mock page here](https://wireframe.cc/6RD0Eq))
, this page contains following sections
  - Patient Details (like name, age etc)
  - List of available templates
  - Patient ReadOnly Data
  - Section which loads selected CRF template (on which curator is working)
