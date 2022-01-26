from django.shortcuts import render,redirect
from .models import Car
from .forms import Arabaform
def merhaba (request):
    liste = Car.objects.all()
    return render(request, 'araba/giris.html', {'Arabalar':liste})

def ekle (request):
    #form = Ulkeform()
    if request.method == 'POST':
        form = Arabaform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Arabaform()
    return render(request, 'araba/ekle.html', {'form':form})

def sil(request,id):
    kayit = Car.objects.get(id=id)
    kayit.delete()
    return redirect('/')