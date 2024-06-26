from django import forms
from .models import CustomUser


class RegisterUserForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name', 'date_of_birth',)
        labels = {
            'username':'Nickname',
            'email':'Email', 
            'password':'Hasło', 
            'password_confirmation':'Powtórz hasło', 
            'first_name':'Imię', 
            'last_name':'Nazwiśko',
            'date_of_birth':'Data urodzenia'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class':'form-control',
                'type': 'date'
            })
        }
        
    def clean(self):
        cleaned_data=super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password= cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Użytkownik o podanym loginie już istnieje')
        
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Użytkownik o podanym email już istnieje')
        
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError('Podane hasła róznią się')
        
        return cleaned_data
    
    

class LoginUserForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'hasło'
    }))
    
    
class SearchUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    
    
class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'hasło'
    }))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'hasło'
    }))

    def clean(self):
        cleaned_data=super().clean()
        password= cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError('Podane hasła róznią się')
        
        return cleaned_data
    

class UserInfoUpdateForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Powtórz hasło'
    }))
        
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture', 'description', 'password', 'password_confirmation',]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Imię'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwiśko'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class':'form-control',
                'placeholder': 'Zdięcie'
            }),
            'description':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'O sobię'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'password'
            }),
        }
        
        