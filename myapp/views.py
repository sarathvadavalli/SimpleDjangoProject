from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        return HttpResponse("We will reach out to you soon..")

    return render(request, 'contact.html')