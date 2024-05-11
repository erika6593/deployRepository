from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ニックネーム')
    email = forms.EmailField(label='Emailアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("このパスワードは短すぎます。最低 8 文字以上必要です。")
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    # def save(self, commit=False):
    #     user = super().save(commit=False)
    #     validate_password(self.cleaned_data['password'], user)
    #     user.set_password(self.cleaned_data['password'])
    #     user.save()
    #     return user


# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label='メールアドレス')
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='メールアドレス:',
        widget=forms.EmailInput(attrs={'autocomplete': 'username'})
    )
    password = forms.CharField(
        label='パスワード:',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )
    remember = forms.BooleanField(
        label='ログイン状態を保持する',
        required=False,
        widget=forms.CheckboxInput(attrs={'autocomplete': 'off'})
    )