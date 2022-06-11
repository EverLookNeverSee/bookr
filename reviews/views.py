from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def search(request):
    qr = request.GET.get("search")
    return render(request, "search_result.html", {"search_query": qr})
