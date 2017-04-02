from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render


def home(request):
    nothing = {}
    if request.method == 'POST':
      	name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        msg = request.POST.get('message', '')
        message = "Hi, I'm " + str(name) + "\n\t Phone : "+ str(phone)+ "\n\t Email : "+ str(email)+ "\n\nMessage:\n\n"+ str(msg)
      	from_email=settings.EMAIL_HOST_USER
        me="rajiv97j@gmail.com"
        to_list =[me]
        send_mail('test mail',message,from_email,to_list,fail_silently = True)
        return HttpResponseRedirect('/')
      
    
    else:
     	
	    return render(request,'home/index.html',context=nothing)





