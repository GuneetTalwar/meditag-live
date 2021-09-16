from django.shortcuts import render,redirect
from .forms import addUserInfo,CreateUserForm,UploadDocumentForm
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile,UploadDocument
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.contrib import messages
# Create your views here.
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def displayDocuments(request,pk):
    allow= False
    info= UserProfile.objects.get(id=pk)
    num = ""
    if request.user.is_authenticated:

        check_info = UserProfile.objects.get(user=request.user)
        num = check_info.id
        if str(check_info.id) == pk:

            allow= True

    docs = info.user.documents.all()
    return render(request,"basic_qr/display_documents.html",{'docs':docs,'allow':allow,'num':num})

def uploadDocument(request):

    if request.method == 'POST':

        form = UploadDocumentForm(request.POST,request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            form.save()

        pk = UserProfile.objects.get(user=request.user).id
        return redirect("basic_qr:display-documents",pk)
    else:
        form = UploadDocumentForm()
    return render(request, "basic_qr/upload-document.html",{'form':form})

def updateDocument(request,pk):
    document = UploadDocument.objects.get(id=pk)
    form = UploadDocumentForm(instance=document)

    if request.method == 'POST':
        form = UploadDocumentForm(request.POST,request.FILES,instance=document)

        if form.is_valid():
            form.save()
        pk = UserProfile.objects.get(user=request.user).id
        return redirect("basic_qr:display-documents",pk)
    return render(request, "basic_qr/upload-document.html",{'form':form})

def deleteDocument(request,pk):
    document = UploadDocument.objects.get(id=pk)
    document.delete()
    ID = UserProfile.objects.get(user=request.user).id
    return redirect("basic_qr:display-documents",ID)

def medform(request):

    if request.method == 'POST':
        phone = request.POST.get('contact_no')
        form = addUserInfo(request.POST)
        if form.is_valid():
            form.save()
        info = UserProfile.objects.get(contact_no=phone)
        info.user = request.user

        info.save()
        return redirect("basic_qr:profile",info.id)
    else:
        form = addUserInfo()
    return render(request, "basic_qr/med_form.html",{'form':form})

def updateMedform(request,pk):
    profile = UserProfile.objects.get(id=pk)
    form = addUserInfo(instance=profile)

    if request.method == 'POST':
        form = addUserInfo(request.POST,instance=profile)
        if form.is_valid():
            form.save()
        return redirect("basic_qr:profile",pk)
    return render(request, "basic_qr/med_form.html",{'form':form})

def landing(request):
    user = request.user
    info = ""
    if user.is_authenticated:
        info = UserProfile.objects.get(user = user).id

    return render(request,"landing.html",{'num':info})

def faqPage(request):
    return render(request,"basic_qr/faq.html")

def profile(request,pk):
    info = UserProfile.objects.get(id=pk)
    num = ""
    allow= False
    if request.user.is_authenticated:

        check_info = UserProfile.objects.get(user=request.user)
        num = str(check_info.id)
        if str(check_info.id) == pk:

            allow= True

    context = {
    'info':info,
    'num':num,
    'allow':allow,
    'path':"https://medi-tag.herokuapp.com" + str(request.path) ,
    'age': "pending"
    }
    if(info.dob):
        context['age'] = calculate_age(info.dob)
    return render(request,"basic_qr/profile.html",context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username =username, password=password)

        if user is not None:
            login(request,user)
            if UserProfile.objects.filter(user = user).exists():
                profile = UserProfile.objects.get(user = user)
                return redirect("basic_qr:profile",profile.id)

            else:
                return redirect("basic_qr:medform")
        else:
            messages.error(request,"Incorrect username or password",extra_tags="danger")



    return render(request,"basic_qr/login.html")

def logoutUser(request):
    logout(request)
    #messages.info(request, 'User was logged out!')
    return redirect('basic_qr:login')


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        username = request.POST['username']
        if ' ' in username:
            messages.error(request,"The username cannot contain a space",extra_tags="danger")
        if form.is_valid():
            user = form.save()
            messages.success(request,"Registration Successful",extra_tags="success")
            return redirect('basic_qr:login')

    context = {'form':form}
    return render(request,"basic_qr/register.html",context)
