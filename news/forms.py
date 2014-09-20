from django import forms
from django.contrib.auth.forms import UserCreationForm
from news.models import Post, Comment


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")


class PostForm(forms.Form):
    url = forms.CharField(required=True)
    title = forms.CharField(required=True)
    post_text = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = ("username", "url", "categories", "title", "post_text", "thumb")

class CommentForm(forms.Form):
    comment_text = forms.CharField(required=True)

    class Meta:
        model = Comment
        fields = ("post_id", "commenter", "comment_text")
