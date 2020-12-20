from django.db import models
from django.contrib.auth import get_user_model

TAGS = (
    ('people','People'),
    ('pets', 'Pets'),
    ('nature','Nature'),
    ('action','Action'),
    ('lifestyle','Lifestyle'),
)

class Pic(models.Model):
  caption = models.CharField(max_length=50)
  imgLink = models.CharField(max_length=100)
  tag = models.CharField(max_length=20, choices=TAGS, default='people')
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

# to use a like button, we'll need a new class so a user can own the like or else they can like it an infinite number of times

  # def __str__(self):
  #   # This must return a string
  #   return f"The Pic named '{self.name}' is {self.color} in color. It is {self.ripe} that it is ripe."
  #
  # def as_dict(self):
  #   """Returns dictionary version of Pic models"""
  #   return {
  #       'id': self.id,
  #       'name': self.name,
  #       'ripe': self.ripe,
  #       'color': self.color
  #   }
