from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.
class Person(models.Model):
    name = models.CharField(_('name'), max_length=128)
    birthday = models.DateField(_('birthday'))
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return f'{self.name} (birthday={self.birthday})'

    class Meta:
        # Use this class as common information of subclasses
        abstract = True


class Teacher(Person):
    at_work = models.BooleanField(_('at work'), default=True)


class Student(Person):
    graduated = models.BooleanField(_('graduated'), default=False)
