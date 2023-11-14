from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('user', 'like_users')

# 4. CommentForm이 없대서 새로 지정
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post',)