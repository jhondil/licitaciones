import requests
from bs4 import BeautifulSoup

# Crear una sesión
session = requests.Session()

# URL de login
login_url = 'https://community.secop.gov.co/STS/Users/Login/LoginAuthenticate?mkey=7d2412ac_964b_43e0_a2fc_9f190526b453'

# Datos del login
payload = {
    'username': 'Team2024',  # Reemplaza con tu usuario
    'password': 'Team2024+' # Reemplaza con tu contraseña
}

# Hacer POST al formulario de login
response = session.post(login_url, data=payload)
print(response.cookies)
# Verificar si el login fue exitoso
if response.status_code == 200:
    print("Login exitoso!")
else:
    print("Login fallido!")

# URL de la página a la que quieres hacer scraping después del login
scrape_url = 'https://www.secop.gov.co/CO1BusinessLine/Tendering/ContractNoticeManagement/Index'

# Hacer GET a la página protegida
response = session.get(scrape_url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    print(soup)
    
    # Aquí puedes extraer la data que necesites
    
    
    
    # data = soup.find_all('div', class_='alguna_clase')  # Ejemplo de extracción
    # for item in data:
    #     print(item.text)
else:
    print("Error al acceder a la página protegida!")

