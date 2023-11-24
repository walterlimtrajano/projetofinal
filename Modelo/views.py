from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

def home (request):
    aluno = models.Aluno.objects.all()
    return render(request, 'home.html' , {'estudante': aluno})

def sobreosite (request):
   return render(request, 'sobreosite.html')

def home (request):
   return render(request, 'home.html')

def suporte (request):
   return render(request, 'suporte.html')

def page1(request):
    form = forms.AlunoForm(request.Post or None)

    if form.is_valid():
     form.save()
     return  redirect('home')
    else:
       return render(request, 'page1.html', {'form':form})
    
def delete(request, id):
   delete = models.aluno.objects.get(id=id)
   delete.delete()
   return redirect ('home')


