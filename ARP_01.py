import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Função para carregar e processar a imagem selecionada
def processar_imagem():
    caminho_arquivo = filedialog.askopenfilename()  # Abre uma janela de diálogo para selecionar uma imagem
    if caminho_arquivo:
        imagem = cv2.imread(caminho_arquivo)

        tamanho_kernel = (5, 5)  # Tamanho do kernel
        sigma = 1.0    # Desvio padrão
        imagem_filtrada = cv2.GaussianBlur(imagem, tamanho_kernel, sigma)

        # Cria uma janela para exibir ambas as imagens
        cv2.namedWindow('Visualizador de Imagem', cv2.WINDOW_NORMAL)  # Isso permite maximizar e minimizar

        # Adicione rótulos de texto
        fonte = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imagem, 'Imagem Original', (10, 30), fonte, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(imagem_filtrada, 'Imagem Filtrada', (10, 30), fonte, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Empilha as imagens verticalmente com rótulos de texto
        imagem_composta = np.vstack((imagem, imagem_filtrada))

        # Exibe a imagem composta
        cv2.imshow('Visualizador de Imagem', imagem_composta)

        # Aguarde o usuário fechar a janela e manipule a saída
        while True:
            tecla = cv2.waitKey(1)
            if tecla == 27:  # Verifique se a tecla Esc foi pressionada para sair
                cv2.destroyAllWindows()
                root.destroy()  # Fecha a janela de diálogo de arquivo
                root.quit()  # Encerra a aplicação
                break

# Cria uma janela GUI simples
root = tk.Tk()
root.title("Aplicativo de Filtro de Imagem")

# Configura o protocolo para fechar a janela principal
root.protocol('WM_DELETE_WINDOW', root.quit)

# Cria um botão para abrir a janela de diálogo de arquivo
botao_abrir = tk.Button(root, text="Abrir Imagem", command=processar_imagem)
botao_abrir.pack()

# Inicia o loop principal da GUI
root.mainloop()
