from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    instructor=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='course_image/',blank=True,null=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    enrolled_date = models.DateTimeField(auto_now_add=True)