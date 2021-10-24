# djagnofly
Some django exmaples branch by branch

every branch is independent

```shell
Python 3.9.4 (default, Apr 26 2021, 10:27:43) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.28.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from core.models import Teacher, Student

In [2]: import datetime

In [3]: Teacher.objects.create(name='Felix', birthday=datetime.date.today(), at_work=True)
Out[3]: <Teacher: Felix (birthday=2021-10-24)>

In [4]: Student.objects.create(name='Max', birthday=datetime.date.today(), graduated=False)
Out[4]: <Student: Max (birthday=2021-10-24)>

In [5]: [t.id for t in Teacher.objects.all()]
Out[5]: [1]

In [6]: [s.id for s in Student.objects.all()]
Out[6]: [2]

In [7]: from core.models import Person
In [9]: [p.id for p in Person.objects.all()]
Out[9]: [1, 2]

In [10]: [p.name for p in Person.objects.all()]
Out[10]: ['Felix', 'Max']

In [11]: 
```

```shell
(venv) ➜  djangofly git:(django-model-inheritance-simple) ✗ python manage.py dbshell
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
sqlite> .tables
account_user                   core_student                 
account_user_groups            core_teacher                 
account_user_user_permissions  django_admin_log             
auth_group                     django_content_type          
auth_group_permissions         django_migrations            
auth_permission                django_session               
core_person                  
sqlite> .schema core_teacher
CREATE TABLE IF NOT EXISTS "core_teacher" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "core_person" ("id") DEFERRABLE INITIALLY DEFERRED, "at_work" bool NOT NULL);
sqlite> .schema core_student
CREATE TABLE IF NOT EXISTS "core_student" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "core_person" ("id") DEFERRABLE INITIALLY DEFERRED, "graduated" bool NOT NULL);
sqlite> .schema core_person
CREATE TABLE IF NOT EXISTS "core_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "birthday" date NOT NULL, "updated_at" datetime NOT NULL);
sqlite> select * from core_teacher;
1|1
sqlite> select * from core_student;
2|0
sqlite> select * from core_person;
1|Felix|2021-10-24|2021-10-24 13:28:03.586387
2|Max|2021-10-24|2021-10-24 13:28:08.309238
sqlite> 
```