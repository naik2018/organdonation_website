from django.db import models

# Create your models here.

class Donor(models.Model):

    GENDER = (('male','male'),('female','female'))
    BLOOD = (('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-'))
    ORGAN = (('Lungs','Lungs'),('Kidney','Kidney'),('Eyes','Eyes'),('Money','Money'),('Heart','Heart'))

    name = models.CharField(max_length = 30, null = False)
    address = models.TextField(max_length = 500, null = False )
    gender = models.CharField(max_length = 30, choices = GENDER, default = 'Male')
    bloodgrp = models.CharField(max_length = 30, choices = BLOOD,default = 'B+')
    organ = models.CharField(max_length = 30, choices = ORGAN, default = 'organ')
    email = models.EmailField(max_length = 254,null = False, default = ' ')

    def __str__(self):
        return self.name


class Receiver(models.Model):

    GENDER = (('male','male'),('female','female'))
    BLOOD = (('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-'))
    ORGAN = (('Lungs','Lungs'),('Kidney','Kidney'),('Eyes','Eyes'),('Money','Money'),('Heart','Heart'))
    AVAILABILITY = (('Yes','Yes'),('No','No'))
    name = models.CharField(max_length = 30, null = False)
    address = models.TextField(max_length = 500, null = False )
    gender = models.CharField(max_length = 30, choices = GENDER, default = 'Male')
    bloodgrp = models.CharField(max_length = 30, choices = BLOOD,default = 'B+')
    organ = models.CharField(max_length = 30, choices = ORGAN, default = 'organ')
    email = models.EmailField(max_length = 254,null = False, default = ' ')
    availability = models.CharField(max_length = 5, default = 'availability')
    state = models.CharField(max_length = 30, null = False)
    

    def __str__(self):
        return self.name
