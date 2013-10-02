'''
'''
from django.db import models
from django.template import defaultfilters
from django.utils.translation import ugettext_lazy as _


class Entity(models.Model):
    '''Class represents the raw entity contains only key and parent field.
    '''
    parent = models.ForeignKey('Entity', blank=True, null=True,
                               verbose_name=_('parent'))


class Attribute(models.Model):
    '''Represents an entity's attribute description.
    '''
    TYPES = (
        ('e', _('entity')),
        ('i', _('integer')),
        ('d', _('decimal')),
        ('s', _('string')),
        ('t', _('text')),
        ('el', _('entity list')),
        ('ei', _('integer list')),
        ('ed', _('decimal list')),
        ('es', _('string list')),
    )
    entity = models.ForeignKey(Entity)
    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), max_length=64)
    type = models.CharField(_('type'), max_length=2, choices=TYPES)
    null = models.BooleanField(_('is nullable'), default=True)

    def save(self, *args, **kwargs):
        '''Set slug
        '''
        self.slug = defaultfilters.slugify(self.name)
        return super(Attribute, self).save(*args, **kwargs)


class InstanceAttribute(Attribute):
    '''Defines attribute of a single entity
    '''


class TypeAttribute(Attribute):
    '''Defines attribute of all a childs of entity
    '''


class Value(models.Model):
    '''Value of an entity
    '''
    attribute = models.ForeignKey(Attribute, verbose_name=_('attribute'))
    entity = models.ForeignKey(Entity, verbose_name=_('entity'))


class EntityValue(Value):
    '''Value contains pk of an entity
    '''
    value = models.ForeignKey(Entity, verbose_name=_('value'))


class IntegerValue(Value):
    '''Value contains integer
    '''
    value = models.IntegerField(_('value'))


class DecimalValue(Value):
    '''Value contains decimal
    '''
    value = models.DecimalField(_('value'), max_digits=16, decimal_places=4)


class StringValue(Value):
    '''Value contains string with a maximum length of 255 symbols
    '''
    value = models.CharField(_('value'), max_length=255)


class TextValue(Value):
    '''Value contains text
    '''
    value = models.TextField(_('value'))
