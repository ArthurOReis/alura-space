from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html') # Tirando HttpResponse e, usando render, vai fazer com que a função procure um arquivo HTML através de um endereço

def imagem(request):
    return render(request, 'galeria/imagem.html')