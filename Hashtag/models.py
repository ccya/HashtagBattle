from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

# class HashManager(models.Manager):
# 	def increment_counts(self, hashtag, increment_by=1):
		# h1, created = self.get_or_create(name=hashtag,
  #                               defaults={"ct": increment_by})
		# if not created:
		# 	h1.ct += increment_by
		# 	h1.save()
		# return h1.click_count
class HashManager(models.Manager):
    def increment_counts(self, hashtag,increment_by=1):
		h1, created = self.get_or_create(name=hashtag,defaults={"ct": increment_by})
		if not created:
			h1.ct += increment_by
			h1.save()
		return h1.ct
class Hashtag(models.Model):
	name = models.CharField(max_length=30)
	ct = models.BigIntegerField(default = 0)
	# objects = HashManager()
	def __unicode__(self):
		return u'%s %d' % (self.name, self.ct)

