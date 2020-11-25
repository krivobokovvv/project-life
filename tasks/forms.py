from django import forms

from .models import Task

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Reset, Column, Button
from crispy_forms.bootstrap import AppendedText, Alert

from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Alert(content="<strong>Warning!</strong> Best check yo self, you're not looking too good.",
                  css_class='alert-warning'),
            Fieldset(
                _('Main'),
                Row(
                    Column(AppendedText('subject', '$', active=True), css_class='col-md-3'),
                    Column('description'),
                ),
            ),
            Fieldset(
                _('Second'),
                'tags',
                'persons',
                'status',
                'project',
            ),
            ButtonHolder(
                Button('submit', 'Save', input_type='button', css_class='btn-outline-primary'),
                Submit('submit', _('Save'), css_class='btn-outline-primary'),
                Reset('reset', _('Reset'), css_class='btn-outline-danger')
            ),
        )


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
