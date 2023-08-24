# Este script irá acessar os endereços https://dadosabertos.rfb.gov.br/CNPJ/ e https://dadosabertos.rfb.gov.br/CNPJ/regime_tributario/ e irá baixar todos os arquivos .zip disponíveis de forma sequencial. Estes arquivos serão salvos na pasta bin no mesmo diretório deste script.

import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

# urls = ['https://dadosabertos.rfb.gov.br/CNPJ/', 'https://dadosabertos.rfb.gov.br/CNPJ/regime_tributario/']

urls = ['https://dadosabertos.rfb.gov.br/CNPJ/regime_tributario/']

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if '.zip' in link.text:
            print('Baixando arquivo: ' + link.text)
            r = requests.get(url + link.text, stream=True)
            total_size = int(r.headers.get('content-length', 0))
            with open(os.path.join(os.path.dirname(__file__), 'bin', link.text), 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=link.text, ascii=True) as pbar:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
                            f.flush()

print('Download finalizado.')