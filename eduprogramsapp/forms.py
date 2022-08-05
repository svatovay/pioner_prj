from django import forms

from .models import EduProgram


class EduProgramForm(forms.ModelForm):
    class Meta:
        model = EduProgram
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EduProgramForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name[:2] == 'is':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
