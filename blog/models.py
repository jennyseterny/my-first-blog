# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils import timezone

class Post(models.Model):
        
    #la clase que ceramos 
    author = models.ForeignKey('auth.User')
    #todo lo que dice models es una atributo del model
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #def publisher una funcion que creamos nosotros puede tomar cualquier nombre
    def publish(self):
        self.published_date = timezone.now()
        #publishedate 
        self.save()

    def __str__(self):
        return self.title

    # Create your models here.
    #despues tienes hacerle saber que ya se crear los cambois en el blog asi que ve a la consola 
    #python manage.py makemigrations blog
