from django import forms

from .models import Task, Tag


class CreateTaskUserForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
