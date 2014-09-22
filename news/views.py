from robotparser import Entry
import user
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.template import RequestContext
from news.forms import EmailUserCreationForm, NewsForm
from news.models import News
from news.utils import get_query
from news_room import settings


def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {})

def north_america(request):
    news = News.objects.filter(category__contains='North America')
    data = {'news': news}
    return render(request, 'continents_news/north_america.html', data)

def south_america(request):
    news = News.objects.filter(category__contains='South America')
    data = {'news': news}
    return render(request, 'continents_news/south_america.html', data)

def asia(request):
    news = News.objects.filter(category__contains='Asia')
    data = {'news': news}
    return render(request, 'continents_news/asia.html', data)

def europe(request):
    news = News.objects.filter(category__contains='Europe')
    data = {'news': news}
    return render(request, 'continents_news/europe.html', data)

def africa(request):
    news = News.objects.filter(category__contains='Africa')
    data = {'news': news}
    return render(request, 'continents_news/africa.html', data)

def australia(request):
    news = News.objects.filter(category__contains='Australia')
    data = {'news': news}
    return render(request, 'continents_news/australia.html', data)

def news(request):
    news = News.objects.all()
    data = {'news': news}
    return render(request, 'continents_news/news.html', data)

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            News.objects.create(category=form.cleaned_data['category'], url=form.cleaned_data['url'],
                                title=form.cleaned_data['title'], news_text=form.cleaned_data['news_text'], user=request.user)
            return redirect("news")
    else:
        form = NewsForm()
    data = {'form': form}
    return render(request, 'add_news.html', data)

def edit_news(request, news_id):
    item = News.objects.get(id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=item)
        if form.is_valid():
            item.save()
            return redirect("news")
    else:
        form = NewsForm(instance=item)
    data = {"item": item, "form": form}
    return render(request, "edit_news.html", data)

def delete_news(request, news_id):
    item = News.objects.get(id=news_id)
    item.delete()
    return redirect("news")

def search_news(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'news_text',])

        found_entries = News.objects.filter(entry_query).order_by('id')

        for entry in found_entries:
            print entry.category
            print entry.get_category_display()

    return render_to_response("search_news.html", { 'query_string': query_string, 'found_entries': found_entries }, context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website at {}, {} {}'.format(user.date_joined, user.first_name, user.last_name)
            html_content = '<h2>Thanks {} {} for signing up at {}!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

