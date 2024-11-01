
from django import forms
from django.utils.safestring import mark_safe

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


from django import forms
from .models import AddCourse
class AddCourseForm:
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'marks']
