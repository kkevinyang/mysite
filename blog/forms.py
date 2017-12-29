from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    根据模型（model）创建表单，我们只需要在这个表单的Meta类里表明使用哪个模型（model）来构建表单。
    Django将会解析model并为我们动态的创建表单
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class EmailPostForm(forms.Form):
    """
    CharField类型的字段会被渲染成<input type=“text”>HTML元素
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
