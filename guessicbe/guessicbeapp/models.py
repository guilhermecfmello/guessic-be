import uuid
from django.db import models

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img_src = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    debut = models.IntegerField()
    members = models.IntegerField()
    popularity = models.IntegerField()
    gender = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    city_flag = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
