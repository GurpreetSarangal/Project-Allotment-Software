from django.http import HttpRequest, HttpResponse


def main(response):
    return HttpResponse("this is main")