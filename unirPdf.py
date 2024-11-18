from PyPDF2 import PdfMerger
from listarArquivos import listarArquivos
import os
from natsort import natsorted

def juntar_pdfs(lista_de_pdfs, arquivo_saida):
    """
    Junta uma lista de arquivos PDF em um único arquivo.

    :param lista_de_pdfs: Lista com os caminhos dos PDFs a serem unidos.
    :param arquivo_saida: Caminho do arquivo PDF resultante.
    """
    merger = PdfMerger()

    for pdf in lista_de_pdfs:
        merger.append(pdf)

    merger.write(arquivo_saida)
    merger.close()
    print(f"PDFs unidos com sucesso em {arquivo_saida}")

# execução

# Caminho do diretório 'listas' no diretório atual
diretorio_listas = os.path.join(os.getcwd(), "listas")

# Obter a lista de arquivos
listar_arquivos_instance = listarArquivos(diretorio_listas)
arquivos = listar_arquivos_instance.listar_arquivos()

arquivos = natsorted(arquivos, key=str.lower)

print(arquivos)

# Construir a lista de caminhos completos para os PDFs
arquivos_completos = [os.path.join(diretorio_listas, arquivo) for arquivo in arquivos if arquivo.endswith('.pdf')]

# Juntar os PDFs
saida = "listas.pdf"

juntar_pdfs(arquivos_completos, saida)
