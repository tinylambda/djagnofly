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
        ordering = ['name']

# Django does make one adjustment to the Meta class of an abstract base class: before installing the Meta attribute,
# it sets abstract=False. This means that children of abstract base classes don’t automatically become abstract classes
# themselves. To make an abstract base class that inherits from another abstract base class,
# you need to explicitly set abstract=True on the child.


class Teacher(Person):
    at_work = models.BooleanField(_('at work'), default=True)

    class Meta(Person.Meta):
        db_table = 'teachers'


class Student(Person):
    graduated = models.BooleanField(_('graduated'), default=False)

    class Meta(Person.Meta):
        db_table = 'students'
