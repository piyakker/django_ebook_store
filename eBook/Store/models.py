from django.db import models

class Ebook(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    cvr_url = models.CharField(max_length=2048)

    def __str__(self) -> str:
        return self.title
    
class CartItem(models.Model):
    title = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)