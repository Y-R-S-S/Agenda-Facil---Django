from django.shortcuts import render

def senha(request):
    return render(request, 'AgendaFacilapp/senha.html')

def cadastro(request):
    return render(request, 'AgendaFacilapp/cadastro.html')