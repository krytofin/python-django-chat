from django import forms


class LoginForm(forms.Form):
    username  = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class':'form-elem'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-elem'}))
    
    
    
