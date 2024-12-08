from django.db import models

# Create your models here.


class Award(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateField()
    

class Skill(models.Model):
    title = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    git_link = models.URLField()

    def __str__(self) -> str:
        return self.title
    

class Technology(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

class Teammate(models.Model):
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    fullname = models.CharField(max_length=150)
    job = models.CharField(max_length=150)
    introduction = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.fullname


class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title