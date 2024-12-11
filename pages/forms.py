from django import forms
from .models import Login

#class LoginForm(forms.Form):
    # username = forms.CharField(max_length=50, label='name', initial='enter username', disabled=True)
   # password = forms.CharField(max_length=50, label='test', initial='enter password', help_text='write letters and digits',widget=forms.PasswordInput, required=False)

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        #fields= ['username']