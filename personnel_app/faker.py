'''
    # https://faker.readthedocs.io/en/master/
    $ pip install faker # install faker module
    python manage.py flush # delete all exists data from db. dont forget: createsuperuser
    python manage.py shell
    from personnel_app.faker import run
    run()
    exit()
'''

from .models import Personnel, Department
from django.contrib.auth.models import User
import random
from faker import Faker
from django.contrib.auth.models import User

def add_department():
    departments = ["Full Stack", "Data Science", "HR", "Sales", "Marketing", "AWS Devops", "Cyber"]
    for i in departments:
        Department.objects.create(name=i)
    
    print("Departments added")

def add_personnel():
    qs_user = User.objects.all()
    qs_department = Department.objects.all()
    fake = Faker()
    TITLE = (
        ("Team Lead", "LEAD"),
        ("Mid Lead", "MID"),
        ("Junior", "JUN"),
    )
    GENDER =(
            ("Female", "F"),
            ("Male", "M"),
            ("Other", "O"),
            ("Prefer Not Say", "N"),
        )
    for i in range(100):
        data = {}
        data["first_name"] = fake.first_name()
        data["last_name"] = fake.last_name()
        department = random.randint(0,len(qs_department)-1)
        data["department"] = qs_department[department]
        user = random.randint(0,len(qs_user)-1)
        data["added_by"] = qs_user[user]
        title = random.sample(TITLE,1)
        data["title"] = title[0][1]
        gender = random.sample(GENDER,1)
        data["gender"] = gender[0][1]
        data["email"] = f'{data["last_name"]}.{data["first_name"]}@clarusway.com'
        if not (i % 10):
            data["is_staff"] = True

        Personnel.objects.create(**data)
        if data.get("is_staff"):
            user = User.objects.create(username=data["email"], email=data["email"], first_name=data["first_name"], last_name=data["last_name"], is_staff=True)
            user.set_password("qazqwe123")
            user.save()
    
    print("Fake personnel added")

def run():
    print('Fake data generation started')
    add_department()
    add_personnel()
    print('Fake data generation completed')