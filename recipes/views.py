from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {"number": 53}
    return render(request, 'recipes/index.html', data)
