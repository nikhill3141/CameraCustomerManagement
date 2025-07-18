from django.db import models
from django.contrib.auth import get_user_model
# Create your models here

User = get_user_model() 

skills = {
  "cinimatography":"cinimatography",
  "videography":"videography",
  "drowner":"drowner",
}

class Cameramen(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cameramen')
  name = models.CharField()
  cameramen_mobile_no = models.IntegerField()
  skills =models.CharField(max_length=20, choices=skills)
  created_at = models.DateTimeField(auto_now_add=True)


  

def __str__(self):
  return self.name