"""
Módulo responsável por abrir e recuperar dados de um XLSX
"""
import os, shutil

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def importar(caminhoArquivo: str) -> dict[str, list[str]]:
    """
    Importa a planilha
    
    Parameters:
        caminhoArquivo (str): Caminho completo para o arquivo .xlsx.
        
    Returns:
        Um dicionário contendo sucesso/erro e uma mensagem descritiva

    Examples:
        >>> importar("")
        {'erro': ['arquivo não informado']}

        >>> importar('caminho/existe/arquivo.docx')
        {'erro': ['formato não suportado, formato suportado .xlsx']}

        >>> importar('caminho/nao/arquivo.xlsx')
        {'erro': ['arquivo não encontrado']}

        >>> importar('tests/resources/arquivos-teste/arquivo.xlsx')
        {'sucesso': ['arquivo importado']}
    """
    if not caminhoArquivo:
        return {'status': 'erro', 'mensagem': 'arquivo não informado'}
    
    if not os.path.isfile(caminhoArquivo):
        return {'status': 'erro', 'mensagem': 'arquivo não encontrado'}
        
    _, extensao = os.path.splitext(caminhoArquivo)
    
    if extensao != ".xlsx":
        return {'status': 'erro', 'mensagem': 'formato não suportado, formato suportado .xlsx'}
    
   
    shutil.copy(caminhoArquivo, os.path.join(DIR_PATH, 'resources', 'arquivos'))
    return  {'status': 'sucesso', 'mensagem': 'arquivo importado'}


def descrever() -> dict[str, list[dict[str, list[str]]]]:
    """
    Recupera o nome das planilhas contidas no arquivo, o nome dos campos da planilha
    """
   