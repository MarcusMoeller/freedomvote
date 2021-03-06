from django import forms
from core.models import Politician
from core.widgets import ImagePreviewFileInput


class PoliticianForm(forms.ModelForm):
    class Meta:
        model = Politician
        exclude = ['unique_key', 'user']
        widgets = {
            'image': ImagePreviewFileInput()
        }

    def clean_party_other(self):
        data = self.cleaned_data.get('party_other')

        if self.cleaned_data.get('party'):
            data = None

        return data

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PoliticianForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.iteritems():
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'form-control'
                })
            if field_name in ['first_name', 'last_name']:
                field.widget.attrs.update({
                    'readonly' : 'readonly'
                })
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'rows': 2,
                })


class PartyPoliticianForm(forms.ModelForm):
    class Meta:
        model = Politician
        fields = ['first_name', 'last_name', 'email', 'state', 'is_member_of_parliament', 'user']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PartyPoliticianForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.iteritems():
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'form-control'
                })
