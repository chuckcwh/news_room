from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'news_room.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news.views.home', name='home'),
    url(r'^faq/$', 'news.views.faq', name='faq'),
    url(r'^category/$', 'news.views.category', name='category'),
    url(r'^news/$', 'news.views.news', name='news'),
    url(r'^profile/$', 'news.views.profile', name='profile'),
    # url(r'^posts/$', 'news.views.posts', name='posts'),
    # url(r'^posts_add/$', 'news.views.posts_add', name='posts_add'),
    # url(r'^comments_add/$', 'news.views.comments_add', name='comments_add'),

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
