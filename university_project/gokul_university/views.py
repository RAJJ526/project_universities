from django.shortcuts import render
def func(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def course(request):
    return render(request, "course.html")
def admission(request):
    return render(request, "admission.html")
def news(request):
    return render(request, "news.html")
def contact(request):
    return render(request, "contact.html")

# Create your views here.
