from django.db import models
from taggit.managers import TaggableManager


class System(models.Model):
    aliases = models.ManyToManyField('core.Alias')
    hostnames = models.ManyToManyField('core.Hostname')

    tags = TaggableManager()

    def __unicode__(self, *args, **kwargs):
        return '%(alias)s (%(hostname)s)' % { 'alias': ' '.join(self.aliases.all().values_list('name', flat=True)),
                                              'hostname': ' '.join(self.hostnames.all().values_list('name', flat=True)),
                                              }


class Alias(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self, *args, **kwargs):
        return self.name


class Hostname(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self, *args, **kwargs):
        return self.name
