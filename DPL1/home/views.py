from django.shortcuts import render
import django.http
# Create your views here.

def home_view(request):
    # return django.http.Http404("vwh, so all's well")
    return  django.http.HttpResponse("Hello world. Vlad was here!!!")