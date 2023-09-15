from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=30, unique=True)
    
    def __str__(self):
        return f'{self.name}'