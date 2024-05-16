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
