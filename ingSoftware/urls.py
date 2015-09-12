from django.conf.urls import patterns,include, url
from django.contrib import admin
from students import views as contacto_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', contacto_views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^preparatoria/$', contacto_views.PrepaView.as_view(), name='prepa-new'),
)
