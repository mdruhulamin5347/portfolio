from django.db import models

class CarouselModel(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    highlight_title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='carousel_images/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    

class WorkDetails(models.Model):
    complete_project = models.PositiveIntegerField(null=True,blank=True)
    happy_client = models.PositiveIntegerField(null=True, blank=True)
    number_of_coffee = models.PositiveIntegerField(null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return f'{self.complete_project}'
    

class AboutMeModel(models.Model):
    my_intro = models.CharField(max_length=150, null=True, blank=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='aboutme_images/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'
    

class MySkillModel(models.Model):
    skill_name = models.CharField(max_length=50, null=True, blank=True)
    skill_percentage = models.IntegerField(null=True, blank=True)
    last_week = models.IntegerField(null=True, blank=True)
    last_month = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.skill_name}'
    

class ServicesModel(models.Model):
    icon = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    details = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    

class ProjectModel(models.Model):
    project_title = models.CharField(max_length=200, null=True, blank=True)
    project_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.project_name}'
    

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name}'
