from django.db import models

# Create your models here.

class BlogModel(models.Model): 
    title = models.CharField(max_length = 200) 
    description = models.TextField() 
    date_created = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images', blank=True)
  
    def __str__(self): 
        return self.title 
