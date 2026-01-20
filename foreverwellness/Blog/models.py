from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

# limits image size to 2MB
def validate_image_size(file):
    # Limit to 2MB (2 * 1024 * 1024 bytes)
    limit_mb = 2
    if file.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max file size is {limit_mb}MB")
    

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
    image = CloudinaryField('image', allowed_formats=['jpg', 'jpeg'], validators=[validate_image_size], blank=True, null=True)
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
