import sys
from pathlib import Path

def organize_folder(args):
    source = args.source
    destination = args.dest
    mode = args.mode
    dry_run = args.dry_run
    recursive = args.recursive
    config = args.config
    unknown = args.unknown

    # TODO - Remover
    print(f"""
        Source:         {source}
        Destination:    {destination}
        Mode:           {mode}
        Dry-Run:        {dry_run}
        Recursive:      {recursive}
        Config:         {config}
        Unknown:        {unknown}
    """)


def verify_path(caminho, verify_dir = False):
    caminho = Path(caminho)

    # Verificar se o caminho existe
    path_exists(caminho)

    if verify_dir:
        # Verificar se o caminho é pasta
        path_is_dir(caminho)
    
    # Retorna o caminho convertido em Path
    return caminho

# Verifica se um caminho existe
def path_exists(caminho):
    if not caminho.exists():
        fatal_error(f"O caminho não existe: {caminho}", 1)

# Verifica se um caminho é uma pasta
def path_is_dir(caminho):
    if not caminho.is_dir():
        fatal_error(f"O caminho destino não é uma pasta!", 1)

def fatal_error(mensagem, exitCode):
    print(f"Ocorreu um ERRO: {mensagem}", file=sys.stderr)
    sys.exit(exitCode)