from django.core.urlresolvers import resolve
from django.conf import settings


class HtmlSnapshotMiddleware(object):

    def process_request(self, request):
        escaped_fragment = request.GET.get('_escaped_fragment_', None)
        if escaped_fragment != '':
            if escaped_fragment is None:
                return None

        path = escaped_fragment if escaped_fragment else request.path

        view, args, kwargs = resolve(
            path,
            urlconf=settings.AJAX_CRAWLING_URLCONF
        )
        if view:
            kwargs['request'] = request
            return view(*args, **kwargs)
        else:
            return None
