from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import os
import urllib.parse


def index(request):
    # list all files in static file directory, excluding subdirectories
    static_dir = settings.STATICFILES_DIRS[0]
    files_list = os.listdir(static_dir)
    files_list.sort(key=lambda x: x.lower())
    # [(filename, url), (filename, nginx_url, django_url), ...]
    files_urls = []
    for filename in files_list:
        filename_quoted = urllib.parse.quote(filename)
        # files_urls.append([filename, 'static/' + filename_quoted])
        files_urls.append([filename, 'http://10.33.55.1:3355/' + filename_quoted, 'static/' + filename_quoted])
    response = render(request, 'mxplayer/index.html', {'files': files_urls})
    return response
