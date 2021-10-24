# djagnofly
Some django exmaples branch by branch

every branch is independent

```shell
(venv) ➜  djangofly git:(django-model-inheritance-abstract) ✗ python manage.py shell
Python 3.9.4 (default, Apr 26 2021, 10:27:43) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.28.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from core.models import Teacher, Student, Person

In [2]: import datetime

In [3]: Teacher.objects.create(name='Felix', birthday=datetime.date.today(), at_work=True)
Out[3]: <Teacher: Felix (birthday=2021-10-24)>

In [4]: Student.objects.create(name='Max', birthday=datetime.date.today(), graduated=False)
Out[4]: <Student: Max (birthday=2021-10-24)>

In [5]: [t.id for t in Teacher.objects.all()]
Out[5]: [1]

In [6]: [s.id for s in Student.objects.all()]
Out[6]: [1]

In [7]: [p.id for p in Person.objects.all()]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-7-a145e97939f1> in <module>
----> 1 [p.id for p in Person.objects.all()]

AttributeError: type object 'Person' has no attribute 'objects'

In [8]: type(Person)
Out[8]: django.db.models.base.ModelBase

In [9]: type(Teacher)
Out[9]: django.db.models.base.ModelBase

In [10]: 
```

```shell
(venv) ➜  djangofly git:(django-model-inheritance-abstract) ✗ python manage.py dbshell
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
sqlite> .tables
account_user                   core_student                 
account_user_groups            core_teacher                 
account_user_user_permissions  django_admin_log             
auth_group                     django_content_type          
auth_group_permissions         django_migrations            
auth_permission                django_session               
sqlite> .schema core_student
CREATE TABLE IF NOT EXISTS "core_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "birthday" date NOT NULL, "updated_at" datetime NOT NULL, "graduated" bool NOT NULL);
sqlite> .schema core_teacher
CREATE TABLE IF NOT EXISTS "core_teacher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "birthday" date NOT NULL, "updated_at" datetime NOT NULL, "at_work" bool NOT NULL);
sqlite> select * from core_student;
1|Max|2021-10-24|2021-10-24 13:34:37.755721|0
sqlite> select * from core_teacher;
1|Felix|2021-10-24|2021-10-24 13:34:32.343277|1
sqlite> 
```