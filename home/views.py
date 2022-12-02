from django.shortcuts import render

# Create your views here.

def index_home_view(request):
    return render(request,'home/index.html')