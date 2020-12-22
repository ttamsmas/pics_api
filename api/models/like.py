from django.db import models
from django.contrib.auth import get_user_model

class Like(models.Model):
  user_id = models.ForeignKey(
      'User',
      on_delete=models.CASCADE
  )
  pic_id = models.ForeignKey('Pic', on_delete=models.CASCADE, related_name='likes')
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return this.owner
