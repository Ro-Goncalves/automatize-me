from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from automatize_me.ler_xlsx import importar as _importar_xlsx

console = Console()
app = Typer()

@app.command()
def importar_xlsx(    
    arquivo : str = Argument('caminho', help= "Arquivo que será usado no processamento"),
):
    tabela = Table()

    status, mensagem = _importar_xlsx(arquivo).values()

    tabela.add_column(status)
    tabela.add_row(mensagem)

    console.print(f'{status} - {mensagem}\n')
    console.print(tabela)

@app.command()
def escala(
    tonica: str = Argument('C', help='Tônica da Escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da Escala'),
):
    console.print(tonica)