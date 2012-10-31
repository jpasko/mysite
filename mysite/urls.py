from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # A home view:
    url(r'^$', 'mysite.views.home'),

    # An about page:
    url(r'^about/$', 'mysite.views.about'),

    # A contact page:
    url(r'^contact/$', 'mysite.views.contact'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # The blog:
    url(r'^blog/$', 'blog.views.main'),

    # A blog post:
    url(r'^blog/(?P<post_id>\d+)/$', 'blog.views.post'),
)
