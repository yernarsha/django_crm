from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, AddCustomerForm
from .models import Customer

# Create your views here.

def index(request):
    customers = Customer.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect('home')
        else:
            messages.success(request, 'Error logging in')
            return redirect('home')
        
    else:
        return render(request, 'app/index.html', {'customers': customers})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'app/register.html', {'form': form})
    
    return render(request, 'app/register.html', {'form': form})


def get_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        return render(request, 'app/customer.html', {'customer': customer})
    else:
        messages.success(request, "Log in to view that info")
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        messages.success(request, "Deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "Log in to delete that info")
        return redirect('home')
    
def add_customer(request):
    if request.user.is_authenticated:
        form = AddCustomerForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Added successfully")
                return redirect('home')

        return render(request, 'app/add_customer.html', {'form': form})
    else:
        messages.success(request, "Log in to add a customer")
        return redirect('home') 

def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect('home')
        
        return render(request, 'app/update_customer.html', {'form': form})
    else:
        messages.success(request, "Log in to update that info")
        return redirect('home')   