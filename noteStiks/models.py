from django.db import models

# Create your models here.

class Users(models.Model):
    FullName = models.CharField(max_length=20)
    Email = models.EmailField(primary_key=True)
    Pass = models.CharField(max_length=12)

    class Meta:
        db_table = 'users'