from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

admin.autodiscover()


urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'klebercimoveis.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  url(r'^$', TemplateView.as_view(template_name='front/index.html')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^api/', include("app.api_urls")),
  url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
