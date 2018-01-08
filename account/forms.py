from django import forms


class LoginForm(forms.Form):
    """
    使用PasswordInput控件来渲染HTMLinput元素，包含type="password"属性
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

