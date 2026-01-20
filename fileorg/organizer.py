import sys
import shutil
from pathlib import Path

from .report import Report

# Variáveis auxiliares para ajudar na organização dos ficheiros
# Recursive Folders -> Guarda as pastas que vai encontrando à medida que corre o programa
# para as organizar depois, no caso de ter a opção de recursividade activa
# Folders to ignore -> Guarda todas as pastas criadas pelo programa para evitar que, no caso da recursividade estar ativa, o programa entre num loop infinito ao organizar pastas que acabou de criar.
recursive_folders, folders_to_ignore = [], []

def organize_folder(args):
    global recursive_folders, folders_to_ignore
    report = Report()

    # Guardar os argumentos em variáveis para facilitar a leitura e escrita do código
    source = args.source
    destination = args.dest
    mode = args.mode
    dry_run = args.dry_run
    recursive = args.recursive
    config = args.config
    unknown = args.unknown

    # Variáveis auxiliares para ajudar na organização dos ficheiros
    recursive_folders = [source]
    folders_to_ignore = [source, destination]

    # Define se é para mover ou copiar. Apenas para alterar o texto no report
    report.moved_or_copied(mode)

    # Itera cada pasta por níveis (Nivel 1, 2, ...)
    for folder in recursive_folders:
        # Percorre cada ficheiro da pasta atual
        for entry in folder.iterdir():

            if entry.is_dir():
                # se for um diretório, a recursividade estiver ativa e não está na "lista negra", 
                # adicionar nas pastas para analizar recursivamente
                if recursive and entry not in folders_to_ignore:
                    recursive_folders.append(entry)
                continue
        
            if not entry.is_file():
                continue

            # Incrementa em 1 a contagem de ficheiros analizados (Excluíndo pastas)
            report.increase_analized_files()

            # Pega a extensão sem o ponto (Padrão definido inicialmente)
            extension = entry.suffix[1:].lower()
            # Verifica se a extensão está nas configuração selecionada
            
            if extension in config.keys():
                store_file(args, entry, config[extension], report)
            
            # Caso não tenha, decide o que fazer com base na opção --uknown
            else:
                match unknown:
                    # --unknown skip -> Simplesmente ignora o ficheiro
                    case "skip":
                        report.increase_ignored_files()
                        continue
                    # --unknown other || opção padrão -> Manda o ficheiro para uma pasta other
                    case "other":
                        store_file(args, entry, "Other", report)
                    # --unknown extension   -> Cria uma pasta com a extensão do ficheiro,
                    # por exemplo: EXT_pdf ou EXT_rar
                    case "extension":
                        store_file(args, entry, f"EXT_{extension}", report)
                    # Caso default - Nunca irá ser alcançado porque o argparse nunca irá permitir
                    # outra opção mas é uma segurança extra
                    case _:
                        fatal_error("Opção não encontrada", 101)

    report.print_all(dry_run)

def store_file(args, file, folder, report):
    # Cria a nova pasta, caso não exista
    folder = args.dest / folder
    if not args.dry_run: folder.mkdir(exist_ok = True)

    folders_to_ignore.append(folder)

    # Se a opção for mover, move o ficheiro para a nova pasta, caso contrário, copia para a nova pasta
    move_file(file, folder, report, args.dry_run) if args.mode == "move" else copy_file(file, folder, report, args.dry_run)

# Armazenar um ficheiro numa pasta
def move_file(file, folder, report, dry_run = False):
    target = folder / file.name
    if file.resolve() == target.resolve():
        report.increase_ignored_files()
        return
    new_location = verify_repeated_file(target, file)
    if not dry_run: file.replace(new_location)
    report.moved_or_copied_files()
    report.add_category_files(folder.name)
    # print(f"Movido {file.name} para {folder}")

def copy_file(file, folder, report, dry_run=False):
    target = folder / file.name
    if file.resolve() == target.resolve():
        report.increase_ignored_files()
        return
    new_location = verify_repeated_file(target, file)
    if not dry_run: shutil.copy(file, new_location)
    report.moved_or_copied_files()
    report.add_category_files(folder.name)
    # print(f"Copiado {file.name} para {folder / file.name}")

def verify_repeated_file(path, file):
    if not path.exists():
        return path
    
    if path.resolve() == file.resolve():
        return path
    
    stem = path.stem        # nome do ficheiro sem a extensão
    suffix = path.suffix    # extensão
    parent = path.parent    # Pasta pai do ficheiro

    i = 1
    while True:
        new_path = parent / f"{stem} ({i}){suffix}"
        if not new_path.exists():
            return new_path
        i += 1

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