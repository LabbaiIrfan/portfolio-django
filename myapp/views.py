from django.shortcuts import render
from django.contrib import messages
from myapp.models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        if len(name) > 1 and len(name) < 30 and len(email) > 1 and len(email) < 30:
            contact = Contact(name=name, email=email, message=message_content)
            contact.save()
            messages.success(request, 'Thank you for contacting us!')
        else:
            messages.error(request, 'Please ensure that your name and email are between 2 and 30 characters long.')
        
        return render(request, 'portfolio.html')
    
    return render(request, 'portfolio.html')
