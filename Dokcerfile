# Baseada na imagem leve do Python
FROM python:3.10-slim

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar e instalar dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o contêiner
COPY . /app/

# Criar um usuário não-root para rodar a aplicação
RUN useradd -m django
USER django

# Expor a porta onde o Gunicorn rodará
EXPOSE 8000

# Comando padrão (fallback) para rodar o contêiner
CMD ["gunicorn", "base.wsgi:application", "--bind", "0.0.0.0:8000"]