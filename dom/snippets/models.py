from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class NameCategory(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.category}'


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NameCategory,blank=True, null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
      return self.title



class Student(models.Model):
    # Fields to store student information, such as name, enrollment number, etc.
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20, unique=True)
    # Other fields and methods go here
    
    def __str__(self):
        return f"{self.name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('student', 'date')
        
    def __str__(self):
        return f"{self.student}"

