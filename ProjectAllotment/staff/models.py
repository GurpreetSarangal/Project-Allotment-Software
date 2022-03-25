from django.db import models

from collegeAdmin.models import *

class allocationTable(models.Model):
    group = models.CharField(max_length=4, null=True, blank=True)
    student_1 = models.ForeignKey(student, on_delete=models.CASCADE, related_name="first_student") 
    student_2 = models.ForeignKey(student, default=None, on_delete=models.SET_DEFAULT, related_name="second_student", null=True, blank=True)
    project = models.ForeignKey(project, default=None, on_delete=models.SET_DEFAULT)
    guide = models.ForeignKey(guide, default=None, on_delete=models.SET_DEFAULT,null=True, blank=True)

    def __str__(self):
        return f"{self.student_1.session} | {self.project.name} "
