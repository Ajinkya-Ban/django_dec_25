from django.shortcuts import render

# Create your views here.
def Home_Page_View(request):
    return render(request, "myapp/index.html")