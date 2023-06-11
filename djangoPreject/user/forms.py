from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegisterForm(forms.ModelForm):
    # 复写 User 的密码
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查
    def clean_password(self):
        data = self.cleaned_data
        if data.get('password1') == data.get('password2'):
            return data.get('password1')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")