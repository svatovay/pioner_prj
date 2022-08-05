from django.contrib import admin
from .models import Student, SocialStatus, HealthLimitations

admin.site.register(Student)
admin.site.register(SocialStatus)
admin.site.register(HealthLimitations)
