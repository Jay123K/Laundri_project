from django.shortcuts import render,redirect
from .models import Person,Customer
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.detail import  DetailView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def Home(request):
    return render(request,'app1/Templates/app1/home_page.html')


def Login_page(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        if not  Person.objects.filter(username= username).exists():
            return redirect('Login')
        
        if Person.username== username and Person.password == password:
            return redirect('/')
        else:
            return redirect('Login')

    return render (request,'app1/Templates/app1/Login_page.html')


def Register_page(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        username=request.POST.get('username')
        password=request.POST.get('password')
        image=request.FILES.get('image')

        person = Person.objects.filter(username = username)

        if person.exists():
            messages.info(request,'Username already taken')

    
        person=Person.objects.create(
            name=name,
            age=age,
            email=email,
            contact=contact,
            address=address,
            username=username,
            password=password,
            image=image,
        )
        
        person.save()

        messages.info(request,'Account created successfully')

        return redirect('Login')

    return render(request,'app1/Templates/app1/register_page.html')


""" Take the data from Customer and save in the database """
def Add_customer(request):
    if request.method=="POST":
        C_name=request.POST.get('C_name')
        C_address=request.POST.get('C_address')
        C_contact=request.POST.get('C_contact')
        C_email=request.POST.get('C_email')
        C_age=request.POST.get('C_age')
        C_image=request.FILES.get('C_image')

        customer=Customer.objects.create(
            C_name=C_name,
            C_address=C_address,
            C_contact=C_contact,
            C_email=C_email,
            C_age=C_age,
            C_image=C_image,
        )
        customer.save()
        return redirect('/')

    return render(request,'app1/Templates/app1/Add_Customer.html')



"""  List of all Customer from Customer  table """
class PersonList(ListView):
    model=Customer
    template_name='app1/Templates/app1/customer_list.html'
    

def All_rate(request):
    return render(request,'app1/Templates/app1/all_rate.html')


"""  Update the Customer table """
class Customer_Update(UpdateView):
    model=Customer
    fields='__all__'
    template_name='app1/Templates/app1/customer_update.html'
    success_url="/"

class Customer_Detail(DetailView):
    model=Customer
    template_name='app1/Templates/app1/customer_detail.html'



""" Delete the Customer from Customer_table """
class Customer_Delete(DeleteView):
    model=Customer
    template_name='app1/Templates/app1/customer_delete.html'
    success_url="/"