from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import PostIndexForm,PostProjectForm
from .models import PostIndex,PostProject

from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    items=PostIndex.objects.all()
    return render(request, 'index.html',{'items':items})



def post_index(request):
    if request.method == "POST":
        form = PostIndexForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Or render another template if needed
    else:
        form = PostIndexForm()
    
    return render(request, 'form.html', {'form': form})

def detalle_post_index(request,id):
    items=get_object_or_404(PostIndex, id=id)
    return render(request,'detalles_posts.html',{'items':items})



def about_us(request):
    
    return render(request, 'about_us.html')




def post_project(request):
    if request.method == "POST":
        form= PostProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        
    else:
        form = PostProjectForm()
    return render(request,'form.html' ,{'form':form})


def project_list(request):
    items = PostProject.objects.all()
    return render(request, 'project_list.html', {'items': items})

def details_projects(request,id):
    items=get_object_or_404(PostProject, id=id)
    return render(request,'detalles_posts.html',{'items':items})


def our_services(request):
    
    return render(request, 'services.html')



def faqs(request):    
    return render(request, 'faqs.html')



def contact(request):
    
    return render(request, 'contact.html')




from .forms import JobOpeningForm

def post_jobopening(request):
    if request.method == 'POST':
        form = JobOpeningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobopening_list')  # You can define this route/page
    else:
        form = JobOpeningForm()
    return render(request, 'form.html', {'form': form}) 



from .models import JobOpening

def jobopening_list(request):
    items = JobOpening.objects.filter(is_active=True).order_by('-posted_at')
    return render(request, 'jobopening_list.html', {'items': items})





from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Process the form data, e.g., send an email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Message: {message}\nPhone: {phone}\nEmail: {email}',
                'atelierjlw@gmail.com',  # From email
                ['atelierjlw@gmail.com'],  # To email
                fail_silently=False,
            )
            
            
            messages.success(request, 'Email Sent! | Mensaje Enviado!')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'enviar_email.html', {'form': form})
