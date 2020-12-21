from django.db import models

class Like(models.Model):
    user = models.ForeignKey(User)
    pic = models.ForeignKey(Pic)
    created = models.DateTimeField(auto_now_add=True)
    
