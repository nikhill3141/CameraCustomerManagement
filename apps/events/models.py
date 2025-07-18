from django.db import models
from django.contrib.auth import get_user_model
# from cameramen.models import Cameramen


# Create your models here.
User = get_user_model()
class Events (models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event')
  event_name = models.TextField()
  event_description = models.TextField()
  event_date = models.DateField()
  location = models.TextField()
  price = models.IntegerField()
  cameramen = models.ManyToManyField('cameramen.Cameramen', related_name='events_cameramens')
  created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
  return self.event_name