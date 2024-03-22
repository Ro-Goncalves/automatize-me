"""
Módulo responsável por abrir e recuperar dados de um XLSX
"""
import os
import pandas as pd
from pandas import DataFrame

from ..infrastructure.gerenciamento_arquivo import importar_arquivo, validar_planilha

RESOURCES = os.path.join('automatize_me', 'resources', 'arquivos')

def _ler_planilha(nomeArquivo: str) -> DataFrame:
    return pd.read_excel(os.path.join(RESOURCES, f'{nomeArquivo}.xlsx'), sheet_name=None)

def importar_planilha(caminhoArquivo: str) -> dict[str, str]:
    """
    Importa a planilha
    
    Parameters:
        caminhoArquivo (str): Caminho completo para o arquivo .xlsx.
        
    Returns:
        Um dicionário contendo sucesso/erro e uma mensagem descritiva
    
    """
    validar_planilha(caminhoArquivo)
    importar_arquivo(caminhoArquivo)

def descrever_planilha(nomeArquivo: str) -> dict:
    """
    Retorna informações sobre o arquivo .xlsx

    Parameters:
        nomeArquivo (str): Nome do arquivo sem a extensão .xlsx.

    Returns:
        Dicionário com as seguintes chaves:
        - "nome_arquivo": Nome do arquivo
        - "quantidade-planilhas": Quantidade de planilhas encontradas no arquivo
        - "nome-planilha": Nome da planilha
        - "campos-planilha": Nome dos campos da planilha
        - "quantidade-linhas-planilha": quantidade de linhas na planillhas
    """
    descricao = {}
    arquivo = _ler_planilha(nomeArquivo)
    descricao["nome_arquivo"] = f'{nomeArquivo}.xlsx'
    descricao["quantidade_planilhas"] = len(arquivo.keys())
    for i, k in enumerate(arquivo.keys()):
        descricao[f"nome_planilha_{i+1}"] = k
        worksheet = arquivo[k]
        descricao[f"campos_planilha_{i+1}"] = list(worksheet.columns.values)[1:]   # Remove a coluna de índices
        descricao[f"quantidade_linhas_planilha_{i+1}"] = len(worksheet)

    return descricao
