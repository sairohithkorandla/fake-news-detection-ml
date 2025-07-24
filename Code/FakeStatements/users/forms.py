from django import forms
from .models import UserRegisterModel
class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 50}), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size': 50}), required=True, max_length=100)
    username = forms.CharField(widget=forms.TextInput(attrs={'size': 50, 'class': 'special'}), required=True,max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'size': 50}), required=True, max_length=100)
    dob    = forms.DateField()
    gender = forms.CharField(widget=forms.TextInput(attrs={'size': 50}), required=True, max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 52}), required=True, max_length=250)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)


    class Meta():
        model = UserRegisterModel
        fields = '__all__'
