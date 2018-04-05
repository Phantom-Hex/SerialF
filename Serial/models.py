from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    return u'user_{0}/{1}'.format(instance.user.id, filename)


class Type(models.Model):
    type_name = models.CharField(max_length=60)
    type_size = models.CharField(max_length=60)

    @models.permalink
    def get_absolute_url(self):
        return 'type-detail', (), {'pk': self.pk}

    def __str__(self):
        return "{} {}".format(self.type_size, self.type_name.lower())


class Maker(models.Model):
    maker_name = models.CharField(max_length=60)
    maker_type = models.CharField(max_length=40)

    @models.permalink
    def get_absolute_url(self):
        return 'type-detail', (), {'pk': self.pk}

    def __str__(self):
        return "{}".format(self.maker_name)

    def maker_wiki(self):
        return "http://en.wikipedia.com/wiki/{}".format(self.maker_name)


class Device(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, models.CASCADE, related_name='device_type')
    maker = models.ForeignKey(Maker, models.CASCADE, related_name='device_creator')
    SKU = models.CharField(max_length=60)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='img/%Y-%m-%d', null=True, blank=True, default='img/no-img.jpeg')
    checkout = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def checked_out(self):
        if self.checkout is True:
            return "Checked out by: {}".format(self.get_previous_by_created_at())
        else:
            return "Available"

    @models.permalink
    def get_absolute_url(self):
        return 'device-detail', (), {'pk': self.pk}

    def __str__(self):
        return "{}".format(self.name)


class UserLoginForm(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email
