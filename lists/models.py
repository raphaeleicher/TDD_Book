from django.db import models

# ToDo: Adjust model so that items are associated with diffrent lists


class List(models.Model):
    pass


class Item(models.Model):
    list = models.ForeignKey(List, default=None)
    text = models.TextField(default='')
