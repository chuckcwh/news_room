from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news.views.home', name='home'),
    url(r'^profile/$', 'news.views.profile', name='profile'),
    url(r'^faq/$', 'news.views.faq', name='faq'),
    url(r'^news/$', 'news.views.news', name='news'),
    url(r'^add_news/$', 'news.views.add_news', name='add_news'),
    url(r'^search_news/$', 'news.views.search_news', name='search_news'),
    url(r'^news/(?P<news_id>\w+)/edit/$', 'news.views.edit_news', name='edit_news'),
    url(r'^news/(?P<news_id>\w+)/delete/$', 'news.views.delete_news', name='delete_news'),

    # url(r'^posts/$', 'news.views.posts', name='posts'),
    # url(r'^posts_add/$', 'news.views.posts_add', name='posts_add'),
    # url(r'^comments_add/$', 'news.views.comments_add', name='comments_add'),

    url(r'^north_america/$', 'news.views.north_america', name='north_america'),
    url(r'^south_america/$', 'news.views.south_america', name='south_america'),
    url(r'^asia/$', 'news.views.asia', name='asia'),
    url(r'^europe/$', 'news.views.europe', name='europe'),
    url(r'^africa/$', 'news.views.africa', name='africa'),
    url(r'^australia/$', 'news.views.australia', name='australia'),


    url(r'^register/$', 'news.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


)
