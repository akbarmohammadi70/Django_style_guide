from django.db import models
from django_style_guide.common.models import BaseModel
 # Create your models here.



class Product(BaseModel):
    name = models.TextField(max_length=255)