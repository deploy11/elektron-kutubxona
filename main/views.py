from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import UpdateView
# Create your views here.
@login_required(login_url='login')
def home(request):
    formulyar = Formulyar.objects.filter(user=request.user)
    form = ''
    q = ''
    if 'q' in request.GET:
            q = request.GET['q']
            formulyar = formulyar.filter(Q(name__icontains=q)) 
            print(formulyar)
    else:
         
         form = DweetForm()
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()    
    return render(request,'home.html',{'formulyar':formulyar,'form':form,'q':q})
class EditView(UpdateView):
     model = Formulyar
     template_name = 'edit.html'
     fields = ['books']
      