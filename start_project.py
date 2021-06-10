import os

WORKDIR = os.getcwd()

os.chdir(WORKDIR)
os.system(f"pip install virtualenv && virtualenv venv && venv\\Scripts\\activate && pip install django && pip install django-allauth && cd Project1 && python manage.py runserver")