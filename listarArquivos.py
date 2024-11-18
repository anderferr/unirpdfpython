import os

class listarArquivos:
    def __init__(self, diretorio):
        self.diretorio = diretorio
        
    def listar_arquivos(self) -> (list[str] | list):
        """
        Retorna uma lista com os nomes dos arquivos em um diretório.

        :param diretorio: Caminho para o diretório.
        :return: Lista com os nomes dos arquivos.
        """
        try:
            return [arquivo for arquivo in os.listdir(self.diretorio) if os.path.isfile(os.path.join(self.diretorio, arquivo))]
        except FileNotFoundError:
            print(f"O diretório '{self.diretorio}' não foi encontrado.")
            return []
        except PermissionError:
            print(f"Sem permissão para acessar o diretório '{self.diretorio}'.")
            return []