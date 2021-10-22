# djagnofly
Some django exmaples branch by branch

every branch is independent

```shell
(venv) ➜  djangofly git:(django-model-inheritance) ✗ python manage.py dbshell
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
sqlite> .schema core_person
CREATE TABLE IF NOT EXISTS "core_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "birthday" date NOT NULL, "updated_at" datetime NOT NULL);
sqlite> .schema core_student
CREATE TABLE IF NOT EXISTS "core_student" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "core_person" ("id") DEFERRABLE INITIALLY DEFERRED, "graduated" bool NOT NULL);
sqlite> .schema core_teacher
CREATE TABLE IF NOT EXISTS "core_teacher" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "core_person" ("id") DEFERRABLE INITIALLY DEFERRED, "at_work" bool NOT NULL);
sqlite> 
```

```shell
Python 3.9.4 (default, Apr 26 2021, 10:27:43) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.28.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from core.models import Student, Teacher, Person

In [2]: p1 = Person.objects.get(id=1)

In [3]: p2 = Person.objects.get(id=2)

In [4]: p1
Out[4]: <Person: ChengCheng (birthday=2016-12-07)>

In [5]: p2
Out[5]: <Person: Gao (birthday=1987-10-22)>

In [6]: p1.teacher
---------------------------------------------------------------------------
RelatedObjectDoesNotExist                 Traceback (most recent call last)
<ipython-input-6-14cfa89edab1> in <module>
----> 1 p1.teacher

~/PycharmProjects/djangofly/venv/lib/python3.9/site-packages/django/db/models/fields/related_descriptors.py in __get__(self, instance, cls)
    419 
    420         if rel_obj is None:
--> 421             raise self.RelatedObjectDoesNotExist(
    422                 "%s has no %s." % (
    423                     instance.__class__.__name__,

RelatedObjectDoesNotExist: Person has no teacher.

In [7]: p1.student
Out[7]: <Student: ChengCheng (birthday=2016-12-07)>

In [8]: p2.teacher
Out[8]: <Teacher: Gao (birthday=1987-10-22)>

In [9]: p2.student
---------------------------------------------------------------------------
RelatedObjectDoesNotExist                 Traceback (most recent call last)
<ipython-input-9-bdb5b9203d0c> in <module>
----> 1 p2.student

~/PycharmProjects/djangofly/venv/lib/python3.9/site-packages/django/db/models/fields/related_descriptors.py in __get__(self, instance, cls)
    419 
    420         if rel_obj is None:
--> 421             raise self.RelatedObjectDoesNotExist(
    422                 "%s has no %s." % (
    423                     instance.__class__.__name__,

RelatedObjectDoesNotExist: Person has no student.

In [10]: 

```