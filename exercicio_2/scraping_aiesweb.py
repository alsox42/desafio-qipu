import warnings
import requests

from pdf2image import convert_from_bytes
from bs4 import BeautifulSoup


warnings.filterwarnings("ignore")
icao_codigo = input("INFORME O CÓDIGO ICAO : ").upper()

url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={icao_codigo}"
response = requests.get(url)

if response.status_code == 200:
    pagina = BeautifulSoup(response.content, 'html.parser')

    nascer_sol = pagina.find('sunrise').text.strip()
    por_sol = pagina.find('sunset').text.strip()
    print(f'NASCER DO SOL ______________: {nascer_sol}')
    print(f'POR DO SOL _________________: {por_sol}')
 
    metar_html = pagina.find('h5', class_='mb-0 heading-primary')
    if metar_html:
        metar_text = metar_html.find_next('p').text.strip()
        print(f"METAR ______________________: {metar_text}")
    else:
        print("Não foi possível encontrar o METAR.")
    
    taf_html = pagina.find('h5', class_='mb-0 heading-primary', text='TAF')
    if taf_html:
        taf_text = taf_html.find_next('p').text.strip()
        print(f"TAF ________________________: {taf_text}")
    else:
        print("Não foi possível encontrar o TAF.")
     
    cartas = pagina.find_all('a', attrs={'title': 'Uso Ostensivo'})
    print(f'TOTAL DE CARTAS DISPONÍVEIS : {len(cartas)}')
    print(f'OBS.: O Download das cartas está disponivel em formato PDF no diretório correte.')

    num_carta=0
    for link in cartas:
      url_carta = link['href']
      response_carta = requests.get(url_carta)
      if response_carta.status_code == 200:
           num_carta+=1
           with open(f'carta{num_carta}.pdf', 'wb') as f:
            f.write(response_carta.content)

           pdf_data = response_carta.content
           imagens = convert_from_bytes(pdf_data)
           imagens[0].show()
      else:
          print(f'Erro ao baixar o arquivo carta{num_carta}.pdf com Status code: {response_carta.status_code}')
    
else:
    print(f"Erro ao fazer a requisição. Código de status: {response.status_code}")