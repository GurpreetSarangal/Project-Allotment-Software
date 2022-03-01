from django.db import models


# Create your models here.
class student(models.Model):
    session = models.CharField(max_length=10)
    rollNo = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    fatherName = models.CharField(max_length=60)
    className = models.CharField(max_length=70)
    email = models.EmailField()
    mobile_1 = models.IntegerField()
    mobile_2 = models.IntegerField()

    def __str__(self):
        return str(self.rollNo) + self.name

class guide(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    mobile_1 = models.IntegerField()
    mobile_2 = models.IntegerField()

    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=60)
    tech = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class staffMember(models.Model):
    name = models.CharField(max_length=60)
    userName = models.CharField(max_length=60, primary_key=True)
    password = models.IntegerField()

    def __str__(self):
        return self.name