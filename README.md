# FileOrganizerCLI

É uma ferramenbto de linha comandos (CLI) desenvolvida em Python para organizar automaticamente ficheiros de uma pasta pela sua extensão. Este programa suporta uma configuração personalizada de organização, modo de simulação, organização recursiva e, no final, um relatório com detalhes no final da execução

## Funcionalidades


Versão Python: 3.12.0


# Exit Codes
    0 - Argumentos passados corretamente e o programa corre normal.
    1 - Caminho não existe ou não é pasta
    2 - Argparse - Argumento inválido / Falta de Argumentos / Opções inválidas / Type Errors / etc
    3 - Problemas ao ler o ficheiro de configuração JSON
    101 - Opção unknown não encontrada

# TODO - Apagar
    echo %ERRORLEVEL% -> Ver exit code Windows