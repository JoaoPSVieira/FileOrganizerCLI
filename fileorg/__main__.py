import argparse

from .organizer import verify_path
from .config import load_config

def parse_args(*arguments):
    parser = argparse.ArgumentParser()

    # Opção --source
    parser.add_argument("--source",
                        required=True,
                        help="Directório origem com os ficheiros por organizar")
    
    # Opção --dest
    parser.add_argument("--dest",
                        help="Directório destino com os ficheiros organizados segundo o ficheiro de configuração especificado. Se não especificado será o mesmo directório que --source")
    
    # Opção --mode
    parser.add_argument("--mode",
                        default="move",
                        choices=["move", "copy"],
                        help="Seleciona se, ao executar o programa, deseja que os ficheiros sejam movidos ou copiados para as novas pastas")
    
    # Opção --dry-run
    parser.add_argument("--dry-run",
                        action="store_true",
                        help="Mostra o que faria ao aplicar o programa mas sem efetuar nenhuma alteração real, apenas mostrando o relatório.")
    
    # Opção --recursive
    parser.add_argument("--recursive",
                        action="store_true",
                        help="Organiza todas as subpastas da origem")
    
    # Opção --config
    parser.add_argument("--config",
                        help="Permite que o utilizador especifique uma configuração diferente da padrão, ao colocar o ficheiro.json com a nova configuração desejada")
    
    # Opção unknown
    parser.add_argument("--unknown",
                        default="other",
                        choices=["skip", "other", "extension"],
                        help="Permite que o utilizador escolha o que ffazer com os ficheiros não identificados. Existem três opções: "
                        "Skip - Ingora os ficheros sem extensão/desconhecidos"
                        "Other - Manda para uma pasta Other"
                        "Extension - Cria pasta com o nome da extensão (ex: EXT_pdf)")

    args = parser.parse_args()

    # Se o destino estiver vazio, usa o mesmo caminho do que o source
    if args.dest is None:
        args.dest = args.source
    
    # Converte o source e dest em Paths, verificando antes disso se existem e se são directórios
    args.source = verify_path(args.source, True)
    args.dest = verify_path(args.dest, True)

    # Verifica se o ficheiros de configuração foi passado com argumento e, se sim, converte-lo em Path
    if args.config is not None:
        args.config = verify_path(args.config)

    # Carrega a configuração que irá ser utilizada para a organizadas dos ficheiros
    args.config = load_config(args.config)

    # TODO - Remover
    print(f"""
        Source:         {args.source}
        Destination:    {args.dest}
        Dry-Run:        {args.dry_run}
        Recursive:      {args.recursive}
        Config:         {args.config}
        Unknown:        {args.unknown}
        """)

def main(*arguments):
    parse_args(arguments)

if __name__ == '__main__':
    main()

