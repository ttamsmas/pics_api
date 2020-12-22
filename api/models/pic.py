from django.db import models
from django.contrib.auth import get_user_model

TAGS = (
    ('People','People'),
    ('Pets', 'Pets'),
    ('Nature','Nature'),
    ('Action','Action'),
    ('Lifestyle','Lifestyle'),
)

class Pic(models.Model):
  caption = models.CharField(max_length=50)
  imgLink = models.CharField(max_length=100)
  tag = models.CharField(max_length=9, choices=TAGS, default='people')
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  users = models.ManyToManyField(
  'User',
  blank=True,
  related_name='pics',
  through='Like',
  through_fields=('pic_id', 'owner_id')
  )

# to use a like button, we'll need a new class so a user can own the like or else they can like it an infinite number of times

  def __str__(self):
    # This must return a string
    return f"The Pic named '{self.caption}' is {self.tag} in color. It is {self.imgLink} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Pic models"""
    return {
        'id': self.id,
        'caption': self.caption,
        'tag': self.tag,
        'imgLink': self.imgLink
    }
