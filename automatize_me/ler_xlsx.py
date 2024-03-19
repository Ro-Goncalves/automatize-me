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
        {'status': 'erro', 'mensagem': 'arquivo não informado'}

        >>> importar('tests/resources/arquivos-teste/arquivo.docx')
        {'status': 'erro', 'mensagem': 'formato não suportado, formato suportado .xlsx'}

        >>> importar('caminho/nao/arquivo.xlsx')
        {'status': 'erro', 'mensagem': 'arquivo não encontrado'}

        >>> importar('tests/resources/arquivos-teste/arquivo.xlsx')
        {'status': 'sucesso', 'mensagem': 'arquivo importado'}
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
