
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import  UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login


def become_vendor(request):
    #check if the form has been submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            Vendor = Vendor.objects.create(name = user.username, created_by = user)
            
            return redirect('frontpage')

    else:
       form = UserCreationForm() 
    
    
    return render( request, "vendor/become_vendor.html", {'form':form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    
    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor})
