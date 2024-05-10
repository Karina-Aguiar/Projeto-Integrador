from django.shortcuts import render
from django.http import HttpResponse
from .models import Doador,Material
from django.shortcuts import redirect


def index(request):
    return render(request, 'home/index.html')


def doador(request):

    if request.method == "GET":
        return render(request,'doador.html')
    
    elif request.method =="POST":
        nome = request.POST.get('vnome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tipo_material = request.POST.getlist('tipo_material')
        unidade_material = request.POST.getlist('unidade_material')
        quantidade = request.POST.getlist('quantidade')

        doador = Doador(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf

        )

        doador.save()

        for tipo_material, unidade_material, quantidade in zip(tipo_material,unidade_material,quantidade):
            material = Material(tipo_material=tipo_material,unidade_material=unidade_material,quantidade=quantidade,doador=doador)
            material.save()
        
        return redirect(doadorResponse)
    
def doadorResponse(request):
    return render(request, 'doador_response.html')
