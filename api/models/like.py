from django.db import models
from django.contrib.auth import get_user_model
from .pic import Pic

class Like(models.Model):
  user_id = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  pic_id = models.ForeignKey(Pic, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def as_dict(self):
    """Returns dictionary version of Pic models"""
    return {
        'id': self.id,
        'caption': self.caption,
        'tag': self.tag,
        'imgLink': self.imgLink
    }
