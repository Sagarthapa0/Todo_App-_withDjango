from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Task(models.Model):
#     title=models.CharField(max_length=85)
#     content=models.CharField(max_length=300)
#     date_posted=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self) -> str:
#         return f"{self.title} whose id is {str(self.id)}"
    
# class Review(models.Model):
#     reviewer_name=models.CharField(max_length=100)
#     review_title=models.CharField(max_length=100)
#     task=models.ForeignKey(Task,on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.review_title

class Task(models.Model):
    title=models.CharField(max_length=100,null=True)
    content=models.CharField(max_length=1000,null=True,blank=True)
    date_posted=models.DateTimeField(auto_now_add=True,null=True)

    user=models.ForeignKey(User,max_length=10,on_delete=models.CASCADE,null=True)
    


    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    profile_pic= models.ImageField(null=True,blank=True,default='Default.jpg')

    user=models.ForeignKey(User,max_length=10,on_delete=models.CASCADE,null=True)
    
    
