from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_page(request):

    return HttpResponse("<h3>测试开发</h3>")
