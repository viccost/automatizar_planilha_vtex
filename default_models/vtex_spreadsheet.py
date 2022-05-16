import abc
from pandas import DataFrame


class VtexSpreadsheet(metaclass=abc.ABCMeta):
    def __init__(self, spreadsheet: DataFrame):
        self.file_name = None
        self.spreadsheet = spreadsheet
        self.lower_headers()

    @abc.abstractmethod
    def colect_data(self):
        """Essa função recebe um DataFrame e percorre as suas linhas, iniciando o mapeamento da planilha de
        especificações, chamando o método responsável por preencher o dicionário para estruturar a planilha de
        especificações."""
        ...

    @abc.abstractmethod
    def fill_lists(self, *args) -> None:
        """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de
               imagens """
        ...

    @abc.abstractmethod
    def build_vtex_spreadsheet(self) -> None:
        """Transforma as informações presentes no dicionário de imagens em listas para transformá-las em linhas e alimentar
                o DataFrame."""
        ...

    @abc.abstractmethod
    def verifications(self, *args) -> None:
        """call the necessaries verifications"""
        ...

    def lower_headers(self) -> None:
        """Change all spreadsheet's keys to lowercase"""
        for key in self.spreadsheet.keys():
            teste = str.lower(key)
            self.spreadsheet.rename(columns={f"{key}": teste}, inplace=True)

    def init_process(self) -> list[str, build_vtex_spreadsheet]:
        """Returns the model's file name and its spreadsheet object."""
        self.colect_data()
        return [self.file_name, self.build_vtex_spreadsheet()]
