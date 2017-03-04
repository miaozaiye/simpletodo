from django.db import models
import datetime

# Create your models here.

class TodoItem(models.Model):
    item = models.CharField(null=True,blank=True,max_length=100)
    STATUS = (
        ('new','new'),
        ('done','done')
    )
    item_status = models.CharField(choices =STATUS,max_length=10)


    def __str__(self):
        return str(self.item)
