from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class Post(models.Model):
    NORTH_AMERICA = 'NA'
    SOUTH_AMERICA = 'SA'
    ASIA = 'AS'
    EUROPE = 'EU'
    AFRICA = 'AF'
    AUSTRALIA = 'AU'
    STATE = (
        (NORTH_AMERICA, "North America"),
        (SOUTH_AMERICA, "South America"),
        (ASIA, "Asia"),
        (EUROPE, "Europe"),
        (AFRICA, "Africa"),
        (AUSTRALIA, "Australia"),
    )
    categories = models.CharField(max_length=2,
                                  choices=STATE,
                                  default=NORTH_AMERICA)

    url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    contributor_id = models.ForeignKey(User, related_name='posts')
    thumb = models.ManyToManyField(User, related_name='posts')

    def __unicode__(self):
        return u"{}".format(self.title)

class Comment(models.Model):
    commenter_id = models.ForeignKey(User, related_name='comments')
    comment_text = models.TextField()
    post_id = models.ForeignKey(Post, related_name='comments')

    def __unicode__(self):
        return u"{}".format(self.comment_text)