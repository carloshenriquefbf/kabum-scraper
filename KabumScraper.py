import requests
import re
from bs4 import BeautifulSoup
from datetime import date


URL = 'https://www.kabum.com.br/produto/104752/placa-de-v-deo-asus-tuf3-nvidia-geforce-gtx-1660-super-14-0-gbps-6gb-gddr6-turing-shaders-tuf-3-gtx1660s-o6g-gaming'
page = requests.get(URL)

pattern = re.compile(r'\{"value"\s*:\s*(\d+)\}')
soup = BeautifulSoup(page.content, 'html.parser')

preconormal = soup.find('div',class_='preco_normal')
precodesconto = soup.find('span',class_='preco_desconto')

today = date.today()

strtoday = str(today)

str1 = str(preconormal.text)
str2 = str(precodesconto.text.replace('à vista',''))


with open("arq.txt", mode='a') as file:
    
    file.write('Data: ' + strtoday + '\nPreço: ' + str1.strip() + '\nPreço à vista: ' + str2.strip() +'\n\n')

file.close()

print("DONE!")

