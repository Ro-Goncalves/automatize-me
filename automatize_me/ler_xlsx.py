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
        >>>importar(caminho/existe/arquivo.xlsx)
        {"sucesso": "arquivo importado"}

        >>>importar(caminho/existe/arquivo.docx)
        {"erro": "formato não suportado"}

        >>>importar()
        {"erro": "arquivo não informado"}

        >>>importar(caminho/nao/arquivo.docx)
        {"erro": "arquivo não encontrado"}
    """
   