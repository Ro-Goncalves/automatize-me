"""
Módulo responsável por gerenciar os arquivos.
"""
import os, shutil
from .variaveis import CAMINHO_ARQUIVOS

def _validar_caminho_vazio(caminhoArquivo: str):
    """
    Verifica se o caminho informado é vazio ou None. Caso positivo, lança uma exceção.
    
    Parameters:
        - caminhoArquivo (str): Caminho do arquivo a ser validado.
        
    Returns:
        Nenhum retorno.

    Raises:
        ValueError: Se o caminho do arquivo for nulo ou vazio.
    """
    if not caminhoArquivo or caminhoArquivo == "":
        raise ValueError("O parâmetro 'caminhoArquivo' não pode estar em branco.")
    
def _validar_caminho_inexistente(caminhoArquivo: str):
    """
    Verifica se o caminho informado  existe. Caso negativo, lança uma exceção.
    
    Parameters:
        - caminhoArquivo (str): Caminho do arquivo a ser validado.
        
    Returns:
        Nenhum retorno. Lança Exceção caso o caminho não exista.    
    """
    if not os.path.exists(caminhoArquivo):
        raise FileNotFoundError(f"Arquivo '{caminhoArquivo}' não foi encontrado.")
    
def _validar_formato_arquivo_planilha(caminhoArquivo: str):
    """
    Verifica se o formato do arquivo é planilha (.xlsx). Caso negativo, lança uma exceção.
    
    Parameters:
        - caminhoArquivo (str): Caminho do arquivo a ser validado.
        
    Returns:
        Nenhum retorno.    
    """
    _, ext = os.path.splitext(caminhoArquivo)
    if ext != ".xlsx":
        raise ValueError(f"A extensão do arquivo deve ser '.xlsx', mas recebeu '{ext}'.")
   
    
def validar_planilha(caminhoArquivo: str):
    """
    Valida um caminho de planilha .xlsx.
    
    Essa função realiza as seguintes verificações:
      * Se o caminho está vazio;
      * Se o caminho existe;
      * Se o caminho aponta para um arquivo com a extensão correta (.xlsx);
      
    Parameters:
        - caminhoArquivo (str): Caminho da planilha a ser validada.
        
    Returns:
        Nenhum retorno.
        
    Raises:
        FileNotFoundError: Se o caminho for inválido ou inexistente.
        ValueError: Se a extensão do arquivo for diferente de ".xlsx" ou o caminho estiver vazio.

    Exemples:
        >>> validar_planilha("")
        Traceback (most recent call last):
            ...
        ValueError: O parâmetro 'caminhoArquivo' não pode estar em branco.

        Exemples:
        >>> validar_planilha('/temp/arquivo.xlsx')
        Traceback (most recent call last):
            ...
        FileNotFoundError: Arquivo '/temp/arquivo.xlsx' não foi encontrado.

        Exemples:
        >>> validar_planilha('teste.txt')
        Traceback (most recent call last):
            ...
        ValueError: A extensão do arquivo deve ser '.xlsx', mas recebeu '.txt'.
    """  
    _validar_caminho_vazio(caminhoArquivo)
    _validar_formato_arquivo_planilha(caminhoArquivo)
    _validar_caminho_inexistente(caminhoArquivo)

def importar_arquivo(caminhoArquivo: str):
    """
    Copia o arquivo passado como paramêtro para "/sources/arquivos"
    Params:
    caminhoArquivo (str): Caminho completo do arquivo a ser movido.
    
    Returns:
        None
    
    Raises:
        ValueError: Caso encontre algum erro ao mover o arquivo.
    """
    try:
        shutil.copy(caminhoArquivo, CAMINHO_ARQUIVOS)        
    except Exception as e:
        raise ValueError("Erro ao mover o arquivo: " + str(e))
    