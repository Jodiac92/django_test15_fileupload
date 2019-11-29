from django.db import models

# Create your models here.
class Document(models.Model):
    docfile = models.ImageField(blank=True)  # imagefile 일반파일이나 이미지 파일을 처리할수있음 ***
    
