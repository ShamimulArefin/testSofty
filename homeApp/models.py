from django.db import models

# Create your models here.
class ShowService(models.Model):
    service_name = models.CharField(max_length=100)
    service_desc = models.CharField(max_length=200)
    service_icon = models.CharField(max_length=100)
    service_box_svg = models.CharField(max_length=5000)
    service_iconbox_color = models.CharField(max_length=100)

    def __str__(self):
        return self.service_name

class ServiceStack(models.Model):
    service_stacks = models.CharField(max_length=500)
    service_stacks_icons = models.CharField(max_length=500)
    service_stacks_icons_color = models.CharField(max_length=300)

    def __str__(self):
        return "stacks"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teamPhotos')
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    sample = models.URLField(blank=True)

    def __str__(self):
        return self.name + " -> " + self.role

class Subscription(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return self.email

class ProjectContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.subject