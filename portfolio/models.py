from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile/')
    birthday = models.CharField(max_length=100)
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance_status = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    about_short = models.TextField()
    about_long = models.TextField()
    intro = models.TextField()
    professions = models.JSONField()  # like ["Designer", "Developer"]

class Stat(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    icon = models.CharField(max_length=100)
    description = models.CharField(max_length=100)



class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Enter percentage between 0 and 100")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"    


class Summary(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name



        
class Education(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    institution = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title





class Experience(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    company = models.CharField(max_length=255)
    responsibilities = models.TextField(help_text="Separate each point with a newline (\\n)")

    def get_responsibilities_list(self):
        return self.responsibilities.split('\n')

    def __str__(self):
        return self.title                        



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name