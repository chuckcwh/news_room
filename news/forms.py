from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news.models import News


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")




class NewsForm(forms.ModelForm):
    NORTH_AMERICA = 'North America'
    SOUTH_AMERICA = 'South America'
    ASIA = 'Asia'
    EUROPE = 'Europe'
    AFRICA = 'Africa'
    AUSTRALIA = 'Australia'
    STATE = (
        (NORTH_AMERICA, "North America"),
        (SOUTH_AMERICA, "South America"),
        (ASIA, "Asia"),
        (EUROPE, "Europe"),
        (AFRICA, "Africa"),
        (AUSTRALIA, "Australia"),
    )
    category = forms.ChoiceField(choices=STATE)

    url = forms.CharField(required=True)
    # news_time = forms.DateTimeField()
    title = forms.CharField(required=True)
    news_text = forms.CharField(required=True)

    class Meta:
        model = News
        fields = ("category", "url", "title", "news_text")

# class CommentForm(forms.Form):
#     comment_text = forms.CharField(required=True)
#
#     class Meta:
#         model = Comment
#         fields = ("post_id", "commenter", "comment_text")