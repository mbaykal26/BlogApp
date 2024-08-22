from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    #blogs = models.ManyToManyField(Blog)  blok kategoriye bağlanabilir!
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    # image = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank= True, unique=True, db_index=True)
    categories = models.ManyToManyField(Category, blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Admin sayfasında title olarak gözükür
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




