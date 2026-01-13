import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_proj_model16.settings")

import django
django.setup()

from ModelApp.models import *
from faker import Faker
from random import *
fake = Faker()

def populate(n):
    for i in range(n):
        feno=randint(101,1000)
        fename=fake.name()
        fesal=randint(10000,99999)
        fesex=fake.random_element(elements=('M','F'))
        fdno=randint(11,14)
        emp_record=Emp.objects.get_or_create(eno=feno,ename=fename,sal=fesal,sex=fesex,dno=fdno)
populate(30)

