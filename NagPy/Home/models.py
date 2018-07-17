from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    website = models.URLField(default="")
    phone = models.IntegerField(default=0)
    dp = models.ImageField(upload_to="dp_pics", blank=True)

    def __str__(self):
        return self.user.username


def create_porfile(sender, **kwargs):
    if kwargs["created"]:
        user_profile = Userprofile.objects.create(user=kwargs["instance"])


post_save.connect(create_porfile, sender=User)


class Event(models.Model):
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=50, default="Nagpur")
    venue = models.CharField(max_length=200, default="")
    date = models.DateField()
    time = models.TimeField()
    contact = models.EmailField(default="")

    def __str__(self):
        return self.name
