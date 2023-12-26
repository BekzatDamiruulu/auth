# models.py

from django.db import models

class RegistrationUser(models.Model):
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirmPassword = models.CharField(max_length=255)
    def __str__(self):
        return f"RegistrationUser(mail={self.mail})"

class Person(models.Model):
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"Person(name={self.mail}, fullname={self.password})"
