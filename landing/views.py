from django.shortcuts import render
from .forms import SubscriberForm
from django.shortcuts import HttpResponseRedirect


def landing(request):
    name = "guitar"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'landing/landing.html', locals())



