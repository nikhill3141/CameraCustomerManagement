from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
  full_name = models.TextField()
  mobile_no = models.IntegerField()
  address = models.TextField()
  order_type = models.TextField()
  order_description = models.TextField()
  total_price = models.IntegerField()
  paid_price = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  @property
  def pending_amount(self):
    return max(self.total_price - self.paid_price, 0)

  def __str__(self):
    return self.full_name