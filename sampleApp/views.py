from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation


def index(request):
    sample_text = _("Hello world from multi language app!")
    return render(request, 'home.html', {'sample_text': sample_text})


def index_tr(request):
    with translation.override("tr"):
        sample_text = _("Hello world from multi language app!")
    return render(request, 'home.html', {'sample_text': sample_text})
