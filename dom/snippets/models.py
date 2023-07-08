from django.db import models
from django.contrib.auth.models import User


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
  


class Room(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message in {self.room} by {self.sender}'





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
        # The unique_together meta flag
        # This means the student and date field cannot have the same value in the database
        # e.g  {student :"azeez",date:"2022/31/12"} and another instance like this {student :"azeez",date:"2022/31/12"} will ❌(fail)
        # e.g  {student :"azeez",date:"2022/31/12"} and another instance like this {student :"lade",date:"2022/31/12"} will ✅(pass)
        # e.g  {student :"azeez",date:"2022/31/12"} and another instance like this {student :"azeez",date:"2023/31/12"} will ✅(pass)
         
        unique_together = ('student', 'date')
        
    def __str__(self):
        return f"{self.student}"


class Todo(models.Model):
    name = models.CharField(max_length=400)
    desription = models.TextField()
    is_present = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"
