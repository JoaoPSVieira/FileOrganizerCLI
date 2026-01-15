import sys
from pathlib import Path

def convert_paths(args):
    origem = Path(args.source)
    destino = Path(args.dest)

    # Verificar se o caminho origem e destino existem
    if not origem.exists():
        error_fatal(f"O caminho origem não existe: {origem}", 1)
    elif not destino.exists():
        error_fatal(f"O caminho destino não existe: {destino}", 1)

    # Verificar se o caminho origem e destino são pastas
    elif not origem.is_dir():
        error_fatal(f"O caminho origem não é uma pasta!", 1)
    elif not destino.is_dir():
        error_fatal(f"O caminho destino não é uma pasta!", 1)

def error_fatal(mensagem, exitCode):
    print(f"Ocorreu um ERRO: {mensagem}", file=sys.stderr)
    sys.exit(exitCode)
    