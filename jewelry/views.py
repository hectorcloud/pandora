from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm
import multiprocessing
from django.contrib import messages


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        multiprocessing.cpu_count()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        messages.success(request, "Switzerland is very rich.")
        messages.success(request, "Austria, How about you?")
        form = ContactForm()

    response = render(request, 'jewelry/index.html', {'form': form})
    response['Content-Disposition'] = "attachment; filename*=utf-8''%e7%be%8e%e5%9b%bdusa.txt"

    return response
