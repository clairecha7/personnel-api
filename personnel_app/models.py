from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Personnel(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="staff")
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    TITLE = (
        ("LEAD", "Team Lead"),
        ("MID", "Mid Lead"),
        ("JUN", "Junior"),
    )

    title = models.CharField(choices=TITLE, max_length=4)

    salary = models.IntegerField(default=80000)

    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Prefer Not To Say"),
    )

    gender = models.CharField(max_length=1, choices=GENDER)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department} {self.first_name} {self.last_name}"