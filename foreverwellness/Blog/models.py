from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Blog(models.Model):
     
    CATEGORY_CHOICES = [
       ('Weight Loss & Detox', 'Weight Loss & Detox'),
       ('Skin Care & Beauty', 'Skin Care & Beauty'),
       ('Digestive Health & Gut Wellness', 'Digestive Health & Gut Wellness'),
       ('Energy, Fitness & Performance', 'Energy, Fitness & Performance'),
       ('Health & Wellness Education', 'Health & Wellness Education'),
       ('Customer Stories & Results', 'Customer Stories & Results'),
       ('Forever Living Business & Lifestyle', 'Forever Living Business & Lifestyle'),
       ('Buying Guides & FAQs', 'Buying Guides & FAQs'),
    ]


    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = CloudinaryField('image', blank=True, null=True)
    excerpt = models.TextField()
    content = CKEditor5Field('Text', config_name='extends')
    posted_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
