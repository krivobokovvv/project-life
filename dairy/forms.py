from django import forms

from .models import Dairy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Reset, Column, Button
from crispy_forms.bootstrap import AppendedText, Alert

from django.utils.translation import gettext_lazy as _

from markitup.widgets import AdminMarkItUpWidget


class DairyForm(forms.ModelForm):
    class Meta:
        model = Dairy
        fields = '__all__'
    
    article = forms.CharField(widget=AdminMarkItUpWidget())
    article_m = forms.CharField(widget=AdminMarkItUpWidget())
'''
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
                Button('submit', _('Save'), input_type='button', css_class='btn-outline-primary'),
                Submit('submit', _('Save'), css_class='btn-outline-primary'),
                Reset('reset', _('Reset'), css_class='btn-outline-danger')
            ),
        )
'''


class UpdateDairyForm(forms.ModelForm):
    class Meta:
        model = Dairy
        fields = '__all__'
