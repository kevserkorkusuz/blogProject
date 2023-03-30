from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email'] 
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.help_text = ''

class ProfilForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'bio', 'image']
    def __init__(self, *args, **kwargs):
        super(ProfilForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

