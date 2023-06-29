import requests
from urllib.parse import urlparse
import socket


print('''
 _____                      __                 _ 
|   __| ___  ___  ___  ___ |  |    ___  ___  _| |
|__   ||  _|| .'||   ||___||  |__ | . ||  _|| . |
|_____||___||__,||_|_|     |_____||___||_|  |___|

                Make a By: Noutz                

[火] https://github.com/Noutzhz

''')

url = input("Digite a URL do site: ")

try:
    response = requests.get(url)
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    print("Domínio:", domain)
    
    # Restante do código para buscar os subdomínios
    
except requests.exceptions.RequestException as e:
    print("Erro de conexão:", e)

def get_subdomains(domain):
    subdomains = []
    try:
        # Realiza uma pesquisa DNS para o domínio fornecido
        _, _, ip_list = socket.gethostbyname_ex(domain)
        for ip in ip_list:
            # Verifica se o endereço IP possui subdomínios
            try:
                subdomain_list = socket.gethostbyaddr(ip)
                subdomains.extend(subdomain_list)
            except socket.herror:
                pass
    except socket.gaierror:
        print("Não foi possível resolver o domínio.")

    return subdomains

# Exemplo de uso
dominio_principal = url
resultado = get_subdomains(dominio_principal)
print("Subdomínios encontrados:")
for subdominio in resultado:
    print(subdominio)
