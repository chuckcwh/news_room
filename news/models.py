from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Category(models.Model):
#     NORTH_AMERICA = 'North America'
#     SOUTH_AMERICA = 'South America'
#     ASIA = 'Asia'
#     EUROPE = 'Europe'
#     AFRICA = 'Africa'
#     AUSTRALIA = 'Australia'
#     STATE = (
#         (NORTH_AMERICA, "North America"),
#         (SOUTH_AMERICA, "South America"),
#         (ASIA, "Asia"),
#         (EUROPE, "Europe"),
#         (AFRICA, "Africa"),
#         (AUSTRALIA, "Australia"),
#     )
#     name = models.CharField(max_length=20,
#                                   choices=STATE,
#                                   default=NORTH_AMERICA)
#
#     def __unicode__(self):
#         return u"{}".format(self.name)



class News(models.Model):
    NORTH_AMERICA = 'North America'
    SOUTH_AMERICA = 'South America'
    ASIA = 'Asia'
    EUROPE = 'Europe'
    AFRICA = 'Africa'
    AUSTRALIA = 'Australia'
    STATE = (
        (NORTH_AMERICA, "North America"),
        (SOUTH_AMERICA, "South America"),
        (ASIA, "Asia"),
        (EUROPE, "Europe"),
        (AFRICA, "Africa"),
        (AUSTRALIA, "Australia"),
    )
    category = models.CharField(max_length=20,
                                  choices=STATE,
                                  default=NORTH_AMERICA)

    url = models.CharField(max_length=200)
    # news_time = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=100)
    news_text = models.TextField()
    user = models.ForeignKey(User, related_name='news')
    # thumb = models.ManyToManyField(User, related_name='news')

    def __unicode__(self):
        return u"{}".format(self.title)





# class Comment(models.Model):
#     commenter_id = models.ForeignKey(User, related_name='comments')
#     comment_text = models.TextField()
#     post_id = models.ForeignKey(Post, related_name='comments')
#
#     def __unicode__(self):
#         return u"{}".format(self.comment_text)