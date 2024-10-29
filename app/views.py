from django.shortcuts import render, redirect
import requests
from .models import Leads
from datetime import datetime


from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome_leads = request.POST.get('nome') 
        whats_app_leads = request.POST.get('whatsapp')
        recebido_em = datetime.now()
        Leads.objects.create(nome_leads=nome_leads,whats_app_leads=whats_app_leads,data_recebimento=recebido_em)

        whats_app_receptor = "5516993379492"
        
        # Montar a mensagem
        message = f"Olá, Adriana! Voçe recebeu novo leads- Nome:{nome_leads} - WhatsApp:{whats_app_leads}<br>Acesse:www.afunimesaocarlos.com.br/accounts/login/adriana/dashboard/"

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
            print('passou oelo return')
        else:
            print("Falha ao enviar a mensagem.")
            # precisa pop up para mostrar a falha de envio

            print(f"Status code: {response.status_code}")
    else:
        print("GET")
        return render(request, 'site/index.html')

def agradecimento(request):
    return render(request, 'site/agradecimento.html')

@login_required
def dashboard(request, user):
    leads = Leads.objects.all().order_by('-data_recebimento')
    return render(request,'site/dashboard.html',{'leads': leads})

@login_required
def login_redirect(request):
    url_redirect = user.username + '/dashboard'
    redirect(url_redirect)





    

