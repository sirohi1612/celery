from django.db import models

# Create your models here.

class Data(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.first_name
