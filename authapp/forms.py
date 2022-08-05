from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import PionerUser


class PionerUserRegisterForm(UserCreationForm):
    class Meta:
        model = PionerUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(PionerUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PionerUserLoginForm(AuthenticationForm):
    class Meta:
        model = PionerUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(PionerUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PionerUserEditForm(UserChangeForm):
    class Meta:
        model = PionerUser
        fields = ('username', 'password', 'email', 'last_login', 'is_superuser',
                  'first_name', 'last_name', 'patronymic', 'birth_date', 'position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # if field_name == 'is_superuser':
            #     field.widget.attrs['class'] = 'form-control form-check-input'
            if field_name == 'password':
                field.widget = forms.HiddenInput()
