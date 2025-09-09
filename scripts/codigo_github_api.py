# CÓDIGO REAL PARA GITHUB API
# Você precisará de um Personal Access Token do GitHub

import requests
import json
import base64

# Configurações
GITHUB_TOKEN = "seu_token_aqui"  # Gere em: Settings > Developer settings > Personal access tokens
GITHUB_USER = "seu-usuario"
REPO_NAME = "atividade01-eucalyptus"

# Headers da API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 1. Criar repositório (se não existir)
repo_data = {
    "name": REPO_NAME,
    "description": "Relatório da Atividade 01 - Análise de Produção de Eucalyptus grandis",
    "homepage": f"https://{GITHUB_USER}.github.io/{REPO_NAME}",
    "public": True,
    "has_pages": True
}

create_repo_response = requests.post(
    "https://api.github.com/user/repos",
    headers=headers,
    json=repo_data
)

# 2. Enviar arquivo HTML
with open('relatorio_github.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

file_data = {
    "message": "Adicionar relatório da Atividade 01 - Análise Eucalyptus grandis",
    "content": base64.b64encode(html_content.encode()).decode(),
    "branch": "main"
}

upload_response = requests.put(
    f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/index.html",
    headers=headers,
    json=file_data
)

# 3. Configurar GitHub Pages
pages_data = {
    "source": {
        "branch": "main",
        "path": "/"
    }
}

pages_response = requests.post(
    f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/pages",
    headers=headers,
    json=pages_data
)

print(f"Repositório criado: {create_repo_response.status_code == 201}")
print(f"Arquivo enviado: {upload_response.status_code == 201}")
print(f"Pages configurado: {pages_response.status_code == 201}")
print(f"URL: https://{GITHUB_USER}.github.io/{REPO_NAME}")
