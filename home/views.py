from django.shortcuts import render
from .models import backendSkills, otherSkills, mlSkills, Projects,experience,certification
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home_view (request):
    backendSkills_list= backendSkills.objects.all()
    otherSkills_list= otherSkills.objects.all()
    mlSkills_list= mlSkills.objects.all()
    Projects_list= Projects.objects.all()
    certification_list = certification.objects.all()
    context = {
        'backendSkills': backendSkills_list,
        'otherSkills': otherSkills_list,
        'mlSkills': mlSkills_list,
        'projects': Projects_list,
        'certification': certification_list,
        'name' : 'Yahya s. Abdallah',
        'description' : 'software engineer',
        'age' : 20,
        'email' : 'yahyasabdallah21@gmail.com',
        'phone' : '+201286200127',
        'education' : 'student at Bachelor of Science in Computer Science from suez-canal university ',
    }
    return render(request, "home.html", context)
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            # Send email
            send_mail(
                f"Message from {name}",
                message,
                email,  # From email
                [settings.EMAIL_HOST_USER],  # To email (your email)
                fail_silently=False,
            )
            
            # Add success message
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            
        except Exception as e:
            # Log the error and show a user-friendly message
            print(f"Error sending email: {str(e)}")  # For debugging
            messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        
        # Redirect to home page with all context data
        return home_view(request)
    
    # If it's a GET request, redirect to home page
    return home_view(request)

def experience_view(request):
    experience_list= experience.objects.all()
    context = {
        'experience': experience_list,
    }
    return render(request, "home.html", context)

def certification_view(request):
    certification_list= certification.objects.all()
    context = {
        'certification': certification_list,
    }
    return render(request, "home.html", context)