from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import contactus


# Create your views here.
def courses(request):
    return render(request,'courses.html')

from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
def contactpagecall(request):
    return render(request, 'contact.html')
# views.py
from django.shortcuts import redirect
from .models import contactus  # Ensure proper import

def contactlogic(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        # Save data to the database using the ContactUs model
        contactus.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            comment=comment
        )
        messages.success(request, "Thank you for your feedback!")
        # Redirect to base1.html (ensure 'base1' is correctly defined in URLs)
        return redirect('base1')



from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from django.contrib import messages  # For success messages

def online_classes(request):
    """
    Handles rendering and submission of the online classes form.
    """
    if request.method == 'POST':
        # Retrieve data from the form
        class_title = request.POST.get('class_title')
        class_link = request.POST.get('class_link')

        # If you need to process the data (e.g., validation or logging), do it here
        if class_title and class_link:
            # Optionally add a success message or perform additional actions
            messages.success(request, "Class submitted successfully!")

        # Redirect to the same page after form submission
        return redirect('online_classes')

    # Render the online_classes.html template
    return render(request, 'online_classes.html')



