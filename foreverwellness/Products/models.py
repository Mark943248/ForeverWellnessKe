from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):

    CATEGORIE_CHOICES = [
        ('Drinks', 'Drinks'),
        ('Bee Products', 'Bee Products'),
        ('Combo Packs', 'Combo Packs'),
        ('Nutritional Supplements', 'Nutritional Supplements'),
    ]



    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    price = models.CharField(max_length=50)
    image = CloudinaryField('image')
    category = models.CharField(max_length=100, choices=CATEGORIE_CHOICES)
    benefits = models.TextField()
    usage = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name