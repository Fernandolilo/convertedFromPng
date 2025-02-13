import sys
import os
import fitz  # PyMuPDF
from PIL import Image
import shutil

def pdf_to_png(input_directory, output_directory):
    # Verifica se o diretório de entrada existe
    if not os.path.exists(input_directory):
        print(f"Erro: O diretório '{input_directory}' não existe.")
        return

    # Verifica se o diretório de saída existe, cria se não existir
    os.makedirs(output_directory, exist_ok=True)

    # Obtém a lista de arquivos PDF no diretório de entrada
    input_files = [f for f in os.listdir(input_directory) if f.lower().endswith(".pdf")]

    # Itera sobre cada arquivo PDF
    for pdf_file in input_files:
        input_path = os.path.join(input_directory, pdf_file)
        
        # Abre o documento PDF
        pdf_document = fitz.open(input_path)

        # Itera sobre cada página e converte para PNG
        for page_index in range(pdf_document.page_count):
            page = pdf_document[page_index]
            pixmap = page.get_pixmap()
            image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            
            # Salva a imagem como PNG no diretório de saída
            output_file_path = os.path.join(output_directory, f"{os.path.splitext(pdf_file)[0]}_page_{page_index + 1}.jpg")
            image.save(output_file_path, "PNG")

            print(f"Página {page_index + 1} do arquivo {pdf_file} salva como {output_file_path}")

        # Fecha o documento PDF
        pdf_document.close()

def install_app():
    # Pergunta ao usuário os diretórios de entrada e saída
    input_folder = input("Digite o caminho do diretório de entrada: ")
    output_folder = input("Digite o caminho do diretório de saída: ")

    # Chama a função com os argumentos fornecidos
    pdf_to_png(input_folder, output_folder)

    print("Instalação concluída.")

if __name__ == "__main__":
    # Verifica se a instalação já foi realizada
    if not os.path.exists("installed.txt"):
        # Se não foi instalado, realiza a instalação
        install_app()

        # Cria um arquivo indicando que a instalação foi realizada
        with open("installed.txt", "w") as file:
            file.write("Installed")
    else:
        print("O aplicativo já está instalado.")
