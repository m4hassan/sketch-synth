from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Controlnet_Form(forms.ModelForm):
    class Meta:
        model = Creations
        fields = ['init_img', 'p_prompt', 'n_prompt']
        widgets = {
            'p_prompt': forms.TextInput(attrs={'class':'text-base p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500" type'}),
            'n_prompt': forms.TextInput(attrs={'class':'text-base p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500" type'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(Controlnet_Form, self).__init__(*args, **kwargs)

        self.fields['init_img'].widget.attrs['class'] = 'hidden'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control flex items-center h-12 px-4 w-64 bg-gray-200 mt-2 rounded focus:outline-none focus:ring-2', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control flex items-center h-12 px-4 w-64 bg-gray-200 mt-2 rounded focus:outline-none focus:ring-2', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control flex items-center h-12 px-4 w-64 bg-gray-200 mt-2 rounded focus:outline-none focus:ring-2', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        # exclude = ('username.help_text', 'password1.help_text')
        # help_texts = {
        #     'username': None,
        #     'password1': None,
        #     'password2': None,
        # }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control flex items-center h-12 px-4 w-64 bg-gray-200 mt-2 rounded focus:outline-none focus:ring-2'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = None

        self.fields['password1'].widget.attrs['class'] = 'form-control flex items-center h-12 px-4 w-64 bg-gray-200 mt-2 rounded focus:outline-none focus:ring-2'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = None
        
        self.fields['password2'].widget.attrs['class'] = 'form-control flex items-center h-12 px-4 w-64 bg-gray-200 mt-2 rounded focus:outline-none focus:ring-2'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = None