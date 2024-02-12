from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.file.name
