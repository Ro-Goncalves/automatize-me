"""
Módulo responsável por abrir e recuperar dados de um XLSX
"""
import os, shutil

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def importar(caminhoArquivo: str) -> dict[str, str]:
    """
    Importa a planilha
    
    Parameters:
        caminhoArquivo (str): Caminho completo para o arquivo .xlsx.
        
    Returns:
        Um dicionário contendo sucesso/erro e uma mensagem descritiva

    Examples:
        >>> importar("")
        {['erro': 'arquivo não informado']}

        >>> importar('caminho/existe/arquivo.docx')
        {'erro': 'formato não suportado, formato suportado .xlsx'}

        >>> importar('caminho/nao/arquivo.xlsx')
        {'erro': 'arquivo não encontrado'}

        >>> importar('tests/resources/arquivos-teste/arquivo.xlsx')
        {'sucesso': 'arquivo importado'}
    """
    if not caminhoArquivo:
        return {'erro': ['arquivo não informado']}
    
    _, extensao = os.path.splitext(caminhoArquivo)
    
    if extensao != ".xlsx":
        return {'status': 'erro', 'mensagem': 'formato não suportado, formato suportado .xlsx'}
    
    if not os.path.isfile(caminhoArquivo):
        return {'erro': ['arquivo não encontrado']}    
   
    shutil.copy(caminhoArquivo, os.path.join(DIR_PATH, 'resources', 'arquivos'))
    return  {'sucesso': ['arquivo importado']}
   