from django.db import models

USER_TYPES = ['Student', 'Resident']
class User(models.Model):
    netid = models.CharField(max_length=6)
    email = models.EmailField()
    password = models.CharField() # TODO how does this work with netid auth
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_type = models.CharField(choices=USER_TYPES, max_length=10)

JOB_CATEGORIES = []
JOB_TYPES = ['Job', 'Service']
class Job(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    category = models.CharField(choices=JOB_CATEGORIES, max_length=20)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=240)
    pay_amount = models.FloatField()
    pay_unit = models.CharField(max_length=10)
    job_type = models.CharField(choices=JOB_TYPES, max_length=7)
    date_posted = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    for_charity = models.BooleanField(default=False)

class Question(models.Model):
    asker = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    text = models.TextField()

class Message(models.Model):
    sender = models.ForeignKey(User)
    recipient = models.ForeignKey(User)
    text = models.TextField()
    job = models.ForeignKey(Job, null=True)
