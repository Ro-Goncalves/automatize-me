"""
Módulo responsável por abrir e recuperar dados de um XLSX
"""

def importar(caminhoArquivo: str) -> dict[str, str]:
    """
    Importa a planilha
    
    Parameters:
        caminhoArquivo (str): Caminho completo para o arquivo .xlsx.
        
    Returns:
        Um dicionário contendo sucesso/erro e uma mensagem descritiva

    Examples:
        >>> importar("")
        {'erro': 'arquivo não informado'}
    """
    if not caminhoArquivo:
        return {'erro': 'arquivo não informado'}
   