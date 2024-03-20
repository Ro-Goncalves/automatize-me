"""
Módulo responsável por abrir e recuperar dados de um XLSX
"""
import os

from .insfrastructure.arquivo import importar_arquivo, validar_planilha

def importar(caminhoArquivo: str) -> dict[str, str]:
    """
    Importa a planilha
    
    Parameters:
        caminhoArquivo (str): Caminho completo para o arquivo .xlsx.
        
    Returns:
        Um dicionário contendo sucesso/erro e uma mensagem descritiva
    
    """
    validar_planilha(caminhoArquivo)
    importar_arquivo(caminhoArquivo)
