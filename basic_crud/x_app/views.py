# import much needed modules
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .models import Contact, Students
from .tokens import account_activation_token


def home(request):
    """
    This function renders the basicaly simple home page
    """
    return render(request, "home.html")


@login_required(login_url="/loginn")
def std_info(request):
    """
    student data insert function that have the functionality of adding the data in database
    """
    if request.method == "POST" and request.method is not "":
        name = request.POST["name"]
        mob = request.POST["mob"]
        email = request.POST["email"]
        addr = request.POST["addr"]
        course = request.POST["course"]
        Students.objects.create(
            name=name, mob=mob, email=email, addr=addr, course=course
        )
        return redirect("show")
    else:
        return render(request, "index.html")


@login_required(login_url="/loginn")
def show(request):
    """
    show function that basically use for the showing tha data of database
    """
    data = Students.objects.all()
    return render(request, "show.html", {"data": data})

@login_required(login_url="/loginn")
def del_data(request, id):
    """
    delete function that delete the data of given specific key by click
    """
    data = Students.objects.get(id=id)
    data.delete()
    return redirect("show")


@login_required(login_url="/loginn")
def edit(request, id):
    """
    edit function that perform to open the database data which are hit by edit button
    """
    data = Students.objects.get(id=id)
    return render(request, "edit.html", {"data": data})


@login_required(login_url="/loginn")
def update(request, id):
    """
    update function that perform the update the data like partially update or single update all perform
    """
    data = Students.objects.get(id=id)
    if request.method == "POST" and request.method is not "":
        name = request.POST["name"]
        mob = request.POST["mob"]
        email = request.POST["email"]
        addr = request.POST["addr"]
        course = request.POST["course"]
        Students.objects.filter(id=id).update(
            name=name, mob=mob, email=email, addr=addr, course=course
        )
        return redirect("show")
    else:
        return redirect("show")


# def register(request):
#     if request.method=='POST' and request.method is not "" :
#         first=request.POST.get('first', '')
#         last=request.POST.get('last', '')
#         user=request.POST.get('user', '')
#         email=request.POST.get('email', '')
#         cpass=request.POST.get('cpass', '')
#         rpass=request.POST.get('rpass', '')
#         super=request.POST.get('super', False)
#         staff=request.POST.get('staff', False)

#         if(cpass==rpass):
#             msg=User.objects.filter(username=user).exists()
#             if(msg):
#                 print("Already Exist")
#                 return redirect('register')
#             else:


#                 # user=User.objects.create(first_name=first,last_name=last,username=user,email=email,password=make_password(rpass),is_superuser=super,is_staff=staff)
#                 # subject = f'welcome {user.last_name}'
#                 # message = f'Hi {user.username}, thank you for registering in student information system.'
#                 # email_from = settings.EMAIL_HOST_USER
#                 # recipient_list = [user.email, ]
#                 # send_mail( subject, message, email_from, recipient_list )
#                 return redirect('start')
#         else:
#             return HttpResponse("<script>alert('Password Not Match');</script>")
#     else:
#         return render(request,'register.html')


def register(request):
    """
    register function that have the functionality of registering the user on the django default given user
    """
    if request.method == "POST":
        first = request.POST.get("first", "")
        last = request.POST.get("last", "")
        username = request.POST.get("user", "")
        email = request.POST.get("email", "")
        cpass = request.POST.get("cpass", "")
        rpass = request.POST.get("rpass", "")
        super_user = request.POST.get("super", False)
        staff = request.POST.get("staff", False)

        if cpass == rpass:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                print("Username already exists")
                return redirect("register")

            # Create a new user instance
            user = User.objects.create(
                first_name=first,
                last_name=last,
                username=username,
                email=email,
                password=make_password(rpass),
                is_superuser=super_user,
                is_staff=staff,
                is_active=False,
            )

            # Send activation email
            current_site = get_current_site(request)
            mail_subject = "Activate your account"
            message = render_to_string(
                "email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse("Please check your email to complete the registration.")
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    else:
        return render(request, "register.html")


def activate(request, uidb64, token):
    """
    activate function that have the functionality of activate the user which are inactive bydefault
    """
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("Thank you for your email confirmation.")
    else:
        return HttpResponse("Activation link is invalid or expired.")


def forget(request):
    """
    forget password function use for reset the password after forget
    """
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            UserModel = get_user_model()
            email = form.cleaned_data["email"]
            associated_users = UserModel.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "pass_reset_email.html"
                    c = {
                        "email": user.email,
                        "domain": request.META["HTTP_HOST"],
                        "site_name": "your site",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            settings.EMAIL_HOST_USER,
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    # return HttpResponse("password reset link send")
                    return redirect("password_reset_done")
    form = PasswordResetForm()
    return render(
        request=request,
        template_name="pass_reset.html",
        context={"password_reset_form": form},
    )


def loginn(request):
    """
    login function which one have the functionality of login the user
    """
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST["password"]
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            request.session["username"] = user.username
            return redirect("start")
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    return render(request, "login.html")


def get_sess(request):
    """
    session function that have the functionality of the get the session
    """
    #  if request.session.has_key('username'):
    #      return request.session['username']
    user = request.session.get("username")
    if user:
        return HttpResponse(f"hello, {user}")
    else:
        return HttpResponse("hello, guest")


def logoutt(request):
    """
    logout function that have the functionality of logout the current user
    """
    logout(request)
    request.session.clear()
    return redirect("start")


def set_cookie(request):
    """
    set cookie function that have the functionality of set the cookie if someone perform the cookie set click
    """
    response = HttpResponse("Cookie Set")
    response.set_cookie("Company", "Chetu India Pvt Ltd", max_age=3000)
    return response


def get_cookie(request):
    """
    get cookie function by with we can get the currenct cookie which are set
    """
    get = request.COOKIES["Company"]
    return HttpResponse(f"Company Name is {get}")


def contact(request):
    """
    contact function with the help of this give the contact us info
    """
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        Contact.objects.create(name=name, email=email, message=message)
        return HttpResponse("Submit succesfully")
    else:
        return render(request, "contact.html")
