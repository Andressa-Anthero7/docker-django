from django.shortcuts import render, redirect
import requests
from .models import Leads
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome_leads = request.POST.get('nome') 
        whats_app_leads = request.POST.get('whatsapp')
        recebido_em = datetime.now()
        Leads.objects.create(nome_leads=nome_leads, whats_app_leads=whats_app_leads, data_recebimento=recebido_em)
        whats_app_receptor = "5516999628815"
        # Montar a mensagem
        message = f"Olá, Adriana! Você recebeu novo lead - Nome: {nome_leads} - WhatsApp: {whats_app_leads}<br>Acesse: www.afunimedsaocarlos.com.br/accounts/login/adriana/dashboard/"

        # Sua API Key fornecida pelo CallMeBot
        api_key = "1271569"  # Substitua pela sua API Key

        # URL da API do CallMeBot (o WhatsApp deve estar no formato internacional)
        url = f'https://api.callmebot.com/whatsapp.php?phone={whats_app_receptor}&text={message}&apikey={api_key}'

        # Enviar a mensagem via requisição GET
        response = requests.get(url)

        # Verificar a resposta
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
            return render(request, 'site/agradecimento.html')
        else:
            print("Falha ao enviar a mensagem.")
            print(f"Status code: {response.status_code}")
            return render(request, 'site/agradecimento.html')
    else:
        return render(request, 'site/index.html')

def agradecimento(request):
    return render(request, 'site/agradecimento.html')

@login_required
def dashboard(request,user):
    leads = Leads.objects.all().order_by('-data_recebimento')
    return render(request, 'site/dashboard.html', {'leads': leads})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_redirect')  # Chama a URL de redirecionamento
        else:
            return render(request, 'registration/login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'registration/login.html')

@login_required
def login_redirect(request):
    username = request.user.username
    url_redirect = f'/accounts/login/{username}/dashboard/'  # URL do dashboard
    return redirect(url_redirect)
