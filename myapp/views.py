from django.shortcuts import render, HttpResponse
from myapp.forms import FormTexto
from django.contrib import messages

def index(request):
    texto = request.POST.get('text_area')
    qualityRadio = request.POST.get('qualityRadio')
    
    form = FormTexto(request.POST)
    if qualityRadio == 'titulo':
        titulo = texto.title()
        print(titulo)
        return render(request, 'html/index.html', {'text': titulo})
    elif qualityRadio == 'maiusculo':
        maiusculo = texto.upper()
        print(maiusculo)
        return render(request, 'html/index.html', {'text': maiusculo})
    elif qualityRadio == 'minusculo':
        minusculo = texto.lower()
        print(minusculo)    
        return render(request, 'html/index.html', {'text': minusculo})
    
    return render(request, 'html/index.html', {'form': form, 'texto': texto})


