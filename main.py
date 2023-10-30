import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os

# Lista de URLs de vídeos
lista_urls = []

def iniciar_download():
    resolucao = resolucao_var.get()
    pasta_destino = pasta_entry.get()

    if not lista_urls:
        resultado_label.config(text="Nenhuma URL de vídeo fornecida.")
        return

    for url in lista_urls.copy():
        try:
            # Crie um objeto YouTube
            yt = YouTube(url)

            # Selecione a resolução desejada
            if resolucao == "alta":
                video_stream = yt.streams.get_highest_resolution()
            else:
                video_stream = yt.streams.get_lowest_resolution()

            # Verifique se a pasta de destino existe, senão, crie-a
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            # Baixe o vídeo
            video_stream.download(output_path=pasta_destino)

            resultado_label.config(text=f"Download do vídeo '{yt.title}' concluído!")
        except Exception as e:
            resultado_label.config(text=f"Erro no download do vídeo '{url}': {str(e)}")

        # Após o download, remova a URL da lista e da listbox
        lista_urls.remove(url)
        url_listbox.delete(0, tk.END)  # Limpe a listbox
        url_listbox.insert(0, lista_urls)  # Preencha a listbox com URLs restantes

def adicionar_url():
    url = url_entry.get()
    if url:
        lista_urls.append(url)
        url_listbox.insert(tk.END, url)
        url_entry.delete(0, tk.END)

def procurar_pasta_destino():
    pasta_destino = filedialog.askdirectory(initialdir="C:/Users/ferna/Downloads")
    pasta_entry.delete(0, tk.END)
    pasta_entry.insert(0, pasta_destino)

# Crie a janela principal
janela = tk.Tk()
janela.title("Baixar Vídeos do YouTube em Sequência")

# Maximize a janela
janela.state('zoomed')

# Crie e posicione os elementos na janela
url_label = tk.Label(janela, text="URL do Vídeo:")
url_label.pack()
url_entry = tk.Entry(janela, width=200)  # Defina um tamanho maior (largura de 200)
url_entry.pack()
adicionar_url_button = tk.Button(janela, text="Adicionar URL", command=adicionar_url)
adicionar_url_button.pack()

url_listbox = tk.Listbox(janela, width=200)  # Defina um tamanho maior (largura de 200)
url_listbox.pack()

resolucao_label = tk.Label(janela, text="Escolha a Resolução:")
resolucao_label.pack()
resolucao_var = tk.StringVar()

# Defina o valor padrão para "alta"
resolucao_var.set("alta")

resolucao_alta = tk.Radiobutton(janela, text="Alta", variable=resolucao_var, value="alta")
resolucao_baixa = tk.Radiobutton(janela, text="Baixa", variable=resolucao_var, value="baixa")
resolucao_alta.pack()
resolucao_baixa.pack()

pasta_label = tk.Label(janela, text="Pasta de Destino:")
pasta_label.pack()
pasta_entry = tk.Entry(janela, width=200)  # Defina um tamanho maior (largura de 200)
pasta_entry.insert(0, "C:/Users/ferna/Downloads")  # Defina o caminho padrão
pasta_entry.pack()
procurar_pasta_button = tk.Button(janela, text="Procurar", command=procurar_pasta_destino)
procurar_pasta_button.pack()

baixar_button = tk.Button(janela, text="Baixar Todos", command=iniciar_download)
baixar_button.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Inicie o loop principal da interface gráfica
janela.mainloop()
