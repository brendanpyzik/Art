from django.shortcuts import render


# Create your views here.
def login(request):
    template = "index.html"
    return render(request, template)


def index(request):
    template = "index.html"
    return render(request, template)


def search(request):
    template = "search.html"
    return render(request, template)


def register(request):
    template = "register.html"
    return render(request, template)


def artist(request):
    template = "artist.html"
    return render(request, template)


def piece(request):
    template = "piece.html"
    return render(request, template)
