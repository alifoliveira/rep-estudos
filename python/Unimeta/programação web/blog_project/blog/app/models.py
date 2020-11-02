from django.db import models

# Create your models here.
class NewPost(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=600)
    creation_date = models.DateField()
    update = models.DateField()
    
    def __str__(self):
        return f"{self.title}, {self.content}, {self.creation_date}, {self.update}"