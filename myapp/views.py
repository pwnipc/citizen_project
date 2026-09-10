from django.shortcuts import render

# Create your views here.
def helloWorld(request):
    context = {"fruits":["Mango", "Apple", "Banana", "Pineaple"], "message":"Hello from Django", "name":"Chalie", "is_authenticated":True}
    return render(request, "index.html", context)

def about(request):
    context = {"message": "This is the about page"}
    return render(request, "about.html", context)