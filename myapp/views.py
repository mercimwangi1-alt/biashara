from django.shortcuts import get_object_or_404, redirect, render
from myapp.models import contact


# Create your views here.
def error_404_view(request, exception):
    return render(request, '404.html', status=404)
def details(request):
    return render(request, 'blog-details.html')
def blog(request):
    return render(request, 'blog.html')

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
def show(request):
    all=Contact.objects.all()
    return render(request, "show.html", {"all":all})

def delete(request, id):
    mycontact = Contact.objects.get(id=id)
    mycontact.delete()
    return redirect('show')
def Edit(request, id):
    editappointment =get_object_or_404(Contact, id=id)

    if request.method == "POST":
        editappointment.name = request.POST.get("name")
        editappointment.email = request.POST.get("email")
        editappointment.message = request.POST.get("message")

        editappointment.save()
        return redirect('/show')

    else:
      return render(request, "edit.html", {'editappointment': editappointment})

    
