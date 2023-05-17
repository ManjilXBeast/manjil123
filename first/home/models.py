from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    grade = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    isbn = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    edition = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    pdf = models.FileField(upload_to='uploads', null=True, blank=False)
    image = models.ImageField(upload_to='uploads', null=True, blank=False)