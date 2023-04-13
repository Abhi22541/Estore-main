
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.contrib import messages
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, force_bytes
from .token import account_activation_token
from .models import Userbase
# Create your views here.
@login_required
def dashboard(request):
    
    return render(request, 'store/accounts/dashboard.html')

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,'store/accounts/edits.html', {'user_form': user_form})

def account_register(request):
      form_class=RegistrationForm
      form=form_class(request.POST or None)
      if request.method=='POST':
              if form.is_valid():
                    user=form.save(commit=False)
                    user.email=form.cleaned_data['email']
                    user.set_password(form.cleaned_data['password'])
                    user.is_active=False
                    user.save()
                    current_site=get_current_site(request)
                    subject='Account Activation'
                    message=render_to_string('store/accounts/activation.html', {
                          'user':user,
                          'domain':current_site.domain,
                          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                          'token':account_activation_token.make_token(user),
                         
					})
                    user.email_user(subject=subject, message=message)
                    return HttpResponse('registered succesfully and activation sent')
              else:
               registerForm = RegistrationForm()
      return render(request, 'store/accounts/register.html', {'form': form})

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Userbase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Userbase.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
         pass
        # user.is_active = True
        # user.save()
        # login(request, user)
        # return redirect('accounts:dashboard')
    else:
        return render(request, 'store/accounts/dashboard.html')


    


        
					
        





































# class Dashboard(View):
#     def get(self, request):
#         products=Product.objects.all()
#         context = {
#             'products':products,
#         }
#         return render(request, 'store/home.html', context) 
    
# # class Registrations(View):
# #     def post(self, request):
# #         form=Userform(request.POST)
# #         if form.is_valid():
# #             user=form.save()
# #             login(request, user)
# #             messages.success("Registration Successfully Completed!!")
# #             return redirect("main:homepage")
# #         messages.error(request, "invalid details provided please check detail again!!")
# #         form=Userform()
# #         return render(request=request, template_name="store/accounts/register.html", context={"registration_form":form})

# def register_request(request):
# 	if request.method == "POST":
# 		form = Userform(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = Userform()
# 	return render (request=request, template_name="store/accounts/register.html", context={"register_form":form})





# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("main:homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="store/accounts/login.html", context={"login_form":form})

