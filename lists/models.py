from django.db import models

# ToDo: Adjust model so that items are associated with diffrent lists


class Item(models.Model):
    text = models.TextField(default='')
