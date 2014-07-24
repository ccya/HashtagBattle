from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from TintProject import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', views.search_form),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^start/$', views.start),
	url(r'^display/$', views.display),
	url(r'^revoke/$',views.revoke),
)
