import sys
from pathlib import Path

def organize_folder(args):
    # Guardar os argumentos em variáveis para facilitar a leitura e escrita do código
    source = args.source
    destination = args.dest
    mode = args.mode
    dry_run = args.dry_run
    recursive = args.recursive
    config = args.config
    unknown = args.unknown

    # Variáveis auxiliares para ajudar na organização dos ficheiros
    recursive_folders, folders_to_ignore = [source], [source]

    # Itera cada pasta por níveis (Nivel 1, 2, ...)
    for folder in recursive_folders:
        # Percorre cada ficheiro da pasta atual
        for file in folder.iterdir():
            # Se o ficheiro for um directório, verifica se a opção recursive foi ativada, se
            # sim guardar o nome das pastas para aplicar-lhes depois recursividade
            if recursive and file.is_dir() and file is not folders_to_ignore:
                recursive_folders.append(file);
                continue
            
            # Pega a extensão sem o ponto (Padrão definido inicialmente)
            extension = file.suffix[1:]
            # Verifica se a extensão está nas configuração selecionada
            if extension in config.keys():
                store_file(file, folder)
            
            # Caso não tenha, decide o que fazer com base na opção --uknown
            else:
                match unknown:
                    # --unknown skip
                    case "skip":
                        continue
                    # --unknown other || opção padrão
                    case "other":
                        print("Manda a other")
                    # --unknown extension
                    case "extension":
                        print("Manda para pasta extension")
                    case _:
                        fatal_error("Opção não encontrada", 101)

    # TODO - Remover
    print(f"""
        {"*" * 20}
        Source:         {source}
        Destination:    {destination}
        Mode:           {mode}
        Dry-Run:        {dry_run}
        Recursive:      {recursive}
        Config:         {config}
        Unknown:        {unknown}
        {"*" * 20}
    """)

# Armazenar um ficheiro numa pasta
def store_file(file, path):
    print(f"Guardado {file.name} in {path}")

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