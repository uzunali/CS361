from django.conf.urls import patterns, include, url
from django.contrib import admin
import myfile.views as ms
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CS361.myfile.views', name='home'),
    url(r'^$', ms.index),
    url(r'base/$', ms.about),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
