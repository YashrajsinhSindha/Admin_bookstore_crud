from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    picture=models.ImageField()
    author=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return str(self.name)+" by "+str(self.author)
        return result

    class Meta:
        db_table='books'