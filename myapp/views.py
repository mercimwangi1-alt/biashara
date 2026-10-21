from django.shortcuts import render




# Create your views here.
def error_404_view(request, exception):
    return render(request, '404.html', status=404)
def details(request):
    return render(request, 'blog-details.html')
def blog(request):
    return render(request, 'blog.html')
def index(request):
    return render(request, 'index.html')
def portfolio(request):
    return render(request, 'portfolio-details.html')
def services(request):
    return render(request, 'services-details.html')
def starter(request):
    return render(request, 'starter-page.html')

from django.shortcuts import render
from .models import Contact

def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "contact.html", {
            "success": "Your message has been saved!"
        })

    return render(request, "contact.html")
    
