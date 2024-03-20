from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from automatize_me.ler_xlsx import importar as _importar_xlsx

console = Console(color_system="truecolor")
app = Typer()

@app.command()
def importar_xlsx(    
    arquivo : str = Argument('caminho', help= "Arquivo que será usado no processamento"),
):
    try:
        _importar_xlsx(arquivo)
        console.print("Arquivo importado com sucesso")
    except Exception as e:
        console.print(e)
   

@app.command()
def escala(
    tonica: str = Argument('C', help='Tônica da Escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da Escala'),
):
    console.print(tonica)