from django.conf.urls import patterns,include, url
from django.contrib import admin
from students import views as contacto_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', contacto_views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sender/',contacto_views.SenderView.as_view(),name='sender') ,
    url(r'^preparatoria/$', contacto_views.PrepaView.as_view(), name='prepa-new'),
    url(r'^profesional/$', contacto_views.ProfeView.as_view(), name='profe-new'),
    url(r'^success/$', contacto_views.SuccessView.as_view(), name='success'),
)
