from django.shortcuts import render, HttpResponse
from .models import Book


def index(request):
    return render(request, "base.html")


def search(request):
    qr = request.GET.get("search")
    return render(request, "search_result.html", {"search_query": qr})


def welcome_view(request):
    message = f"<html><h1>Welcome to Bookr</h1> " \
              f"<p>{Book.objects.count()} books and counting.</p></html>"
    return HttpResponse(message)
