from django.db import models

# Create your models here.
class backendSkills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class otherSkills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class mlSkills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    def __str__(self):
        return self.title
class info(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    education = models.TextField()
    def __str__(self):
        return self.name
class experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
class certification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='certifications/' )
    def __str__(self):
        return self.title
