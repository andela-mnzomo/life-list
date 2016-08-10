from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    """ Creates bucketlist  """

    created_by = models.ForeignKey("auth.User",
                                   related_name="bucketlists",
                                   blank=True)
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title


class Item(models.Model):
    """ Creates bucketlist item """

    created_by = models.ForeignKey("auth.User")
    bucketlist = models.ForeignKey("Bucketlist",
                                   related_name="items",
                                   blank=True)
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
