from django.contrib import admin
from .models import backendSkills, otherSkills, mlSkills, Projects, info, experience, certification
# Register your models here.
admin.site.register(backendSkills)
admin.site.register(otherSkills)
admin.site.register(mlSkills)
admin.site.register(Projects)
admin.site.register(info)
admin.site.register(experience)
admin.site.register(certification)
