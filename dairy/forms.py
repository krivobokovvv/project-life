from django import forms

from .models import Article

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Reset, Column, Button
from crispy_forms.bootstrap import AppendedText, Alert

from django.utils.translation import gettext_lazy as _

from markitup.widgets import MarkItUpWidget


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    
    text = forms.CharField(widget=MarkItUpWidget())
    day = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Second'),
                'id',
                'day',
                'text',
            ),
            ButtonHolder(
                Submit('submit', _('Save'), css_class=''),
                Reset('reset', _('Reset'), css_class='btn-danger')
            ),
        )



class UpdateDairyForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
