from django.contrib import admin

# Register your models here.

from .models import student
from .models import guide
from .models import project
# from .models import ProjectAllotmentTable
from .models import staffMember


admin.site.register(student)
admin.site.register(guide)
admin.site.register(project)
# admin.site.register(ProjectAllotmentTable)
admin.site.register(staffMember)