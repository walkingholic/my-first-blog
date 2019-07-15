from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("설문조사 인덱스 위치 ")
# Create your views here.
