from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

# Meio alternativo para pagina principal ao invez do Redirect View
# def index(request):
#     return redirect('/agenda')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
