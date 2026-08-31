from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

INPUT_CLASSES = ('w-full px-4 py-3 rounded-xl bg-slate-800 border border-slate-700 '
                  'text-white placeholder-slate-400 focus:outline-none '
                  'focus:ring-2 focus:ring-fuchsia-500 transition')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm password',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': INPUT_CLASSES,
                'placeholder': placeholders.get(field_name, ''),
            })


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 3, 'placeholder': 'Tell us a bit about yourself...'}),
        }