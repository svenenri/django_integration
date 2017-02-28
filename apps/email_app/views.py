from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Email

# Views for email validation project
def index(request):

	return render(request, 'email_app/index.html')

def process(request):

	if request.method == 'POST':
		email = request.POST['email']
		checkEmail = Email.emailValidate.validate(email)
		if checkEmail[0] == False:
			messages.error(request, checkEmail[1])
			return redirect('/')
		else:
			messages.success(request, checkEmail[1])
			return redirect(reverse('email_validate:email_valid'))

def success(request):

	try:
		emailGet = Email.emailValidate.getAllEmails()
		context = {
			'emails': emailGet
		}
		return render(request, 'email_app/success.html', context)
	except:
		return redirect(reverse('email_validate:email_index'))

def delete(request, id):

	if request.method == 'POST':
		deleteEmail = Email.emailValidate.delete(id)
		if deleteEmail[0] == True:
			messages.success(request, deleteEmail[1])
			return redirect(reverse('email_validate:email_valid'))
		else:
			messages.error(request, deleteEmail[1])
			return redirect(reverse('email_validate:email_valid'))
