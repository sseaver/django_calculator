from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

ACCESS_LEVELS = [
    ('u', 'User'),
    ('o', 'Owner'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    @property
    def is_owner(self):
        return self.access_level == 'o'


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Operations(models.Model):
    user = models.ForeignKey("auth.User")
    created = models.DateTimeField(auto_now_add=True)
    number1 = models.FloatField()
    number2 = models.FloatField()
    function = models.CharField(max_length=1)
    answer = models.FloatField()
