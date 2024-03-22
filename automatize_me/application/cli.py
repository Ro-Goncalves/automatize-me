from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from automatize_me.service.gerenciamento_planilha import importar_arquivo as _importar_arquivo
from automatize_me.service.gerenciamento_planilha import descrever_planilha as _descrever_planilha

console = Console(color_system="truecolor")
app = Typer()

@app.command()
def importar_planilha(    
    arquivo : str = Argument(..., help= "Arquivo que será usado no processamento"),
):
    try:
        _importar_arquivo(arquivo)
        console.print("Arquivo importado com sucesso")
    except Exception as e:
        console.print(e)
   

@app.command()
def descrever_planilha(
    arquivo: str = Argument(..., help='Nome do Arquivo')
):
    dfs  = _descrever_planilha(arquivo)
    print(dfs)
    