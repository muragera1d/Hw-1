from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет бобер!")


def test(request):
    return HttpResponse("Нифига :)")
