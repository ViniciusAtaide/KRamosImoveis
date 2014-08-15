from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'django_ajax_crawling.views.index'),
    url(r'^lista/$', 'django_ajax_crawling.views.imovel_list'),
    url(r'^completos/$', 'django_ajax_crawling.views.completo_list'),
    url(r'^imovel/(?P<pk>[\d]+)/$', 'django_ajax_crawling.views.imovel'),
    # url(r'^object/(?P<object>.*)/$', 'app.views_html_snapshot.index'),
)
