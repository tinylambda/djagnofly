from django.contrib import admin

# Register your models here.
from .models import Person, Teacher, Student


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'updated_at')


admin.site.register(Person, PersonAdmin)
admin.site.register(Teacher, PersonAdmin)
admin.site.register(Student, PersonAdmin)
