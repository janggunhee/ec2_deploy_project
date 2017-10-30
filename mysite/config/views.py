from django.http import HttpResponse


def index(request):
    return HttpResponse('<html>'
                        '<body>'
                        '<img src="/media/123.jpeg" width="100%">'
                        '</body>'
                        '</html>')
