from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


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

	@models.permalink
	def get_absolute_url(self):
		return 'type-detail', (), {'pk': self.pk}

	def __str__(self):
		return "{}".format(self.maker_name)


class Device(models.Model):
	name = models.CharField(max_length=255)
	type = models.ForeignKey(Type, models.CASCADE, related_name='device_type')
	maker = models.ForeignKey(Maker, models.CASCADE, related_name='device_creator')
	SKU = models.CharField(max_length=60)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	photo = models.ImageField(blank=True, null=True, upload_to="static/images")

	@models.permalink
	def get_absolute_url(self):
		return 'device-detail', (), {'pk': self.pk}

	def __str__(self):
		return "{} ({})".format(self.name, self.type)

	def thumbnail(self):
		return mark_safe(u'<img_src="../%s" />' % self.photo)


class UserLoginForm(models.Model):
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	def __unicode__(self):
		return self.email
