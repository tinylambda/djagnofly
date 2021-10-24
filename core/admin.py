from django.contrib import admin

# Register your models here.
from .models import Teacher, Student


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'updated_at')


admin.site.register(Teacher, PersonAdmin)
admin.site.register(Student, PersonAdmin)
