from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Child)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Task)
admin.site.register(Classroom)