from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    """Home view."""

    return render_to_response('mysite/home.html',
                               RequestContext(request))

def about(request):
    """About view."""

    return render_to_response('mysite/about.html',
                               RequestContext(request))

def contact(request):
    """Contact view."""

    return render_to_response('mysite/contact.html',
                               RequestContext(request))
