# FileOrganizerCLI

É uma ferramenta de linha comandos (CLI) desenvolvida em Python para organizar automaticamente ficheiros de uma pasta pela sua extensão. Este programa suporta uma configuração personalizada de organização, modo de simulação, organização recursiva e, no final, um relatório com detalhes da execução.


## Funcionalidades
- Organização automática de ficheiros por categorias (ex: Documentos, Imagens, Código, etc)
- Suporte a configuração em JSON
- Modo mover ou copiar
- Modo dry-run, em que consiste numa simulação sem alterar ficheiros
- Organização recursiva de subpastas
- Tratamento de ficheiros duplicados
- Relatório final com estatísticas detalhadas


## Estrutura do Projeto
```
fileorg/
├─ fileorg/
│  ├─ __init__.py
│  ├─ __main__.py
│  ├─ config.py
│  ├─ organizer.py
│  └─ report.py
│
├─ tests/
│
├─ config.default.json
├─ README.md
├─ LICENSE
├─ .gitignore
└─ .gitattributes
```


## Requisitos
- Python **3.10+**
- Sistema operativo compatível com a biblioteca `pathlib` (Windows, Linux, macOS)


## Como executar
O programa é executado com um módulo python:

```bash
python -m fileorg --source <PASTA_ORIGEM> [opções]
```

### Exemplo
```bash
python -m fileorg --source ~/Downloads
```
Organiza os ficheiros da pasta `Downloads`, movendo-os para subpastas do mesmo diretório.


## Opções disponíveis

| Opção | Descrição |
|------|----------|
| `--source` | Pasta de origem (obrigatória) |
| `--dest` | Pasta de destino (opcional; por defeito usa a origem) |
| `--mode` | `move` ou `copy` (por defeito: `move`) |
| `--dry-run` | Simula a execução sem alterar ficheiros |
| `--recursive` | Organiza subpastas|
| `--config` | Caminho para ficheiro JSON de configuração |
| `--unknown` | O que fazer com ficheiros desconhecidos (`skip`, `other`, `extension`) |
| `--verbose` | (*POR IMPLEMENTAR*) Mostra informação detalhada durante a execução do programa |
| `--undo` | (*POR IMPLEMENTAR*) Reverte a última organização efetuada, restaurando os ficheiros às localizações originais |


## Configuração personalizada
É possível definir regras próprias de organização num ficheiro JSON.

Exemplo de `config.json`
```json
{
"Imagens": ["jpg", "png", "gif"],
"Documentos": ["pdf", "docx", "txt"],
"Código": ["py", "cpp", "js"]
}
```
Pode utilizar a configuração criada da seguinte forma:
```bash
python -m fileorg --source . --config config.json
```


## Tratamento de ficheiros desconhecidos
A opção `--unknown` define o comportamento para ficheiros sem extensão ou não definidos na configuração dada:

- `skip` → ignora o ficheiro
- `other` → envia para a pasta `Other`
- `extension` → cria uma pasta com o nome da extensão (ex: `EXT_pdf`)


## Relatório final
No final da execução, o programa apresenta:
- Número total de ficheiros analisados
- Ficheiros movidos/copiados
- Ficheiros ignorados
- Contagem por categoria

Em modo `--dry-run`, o relatório mostra apenas o que aconteceria (Simulação)

##  Exit Codes
    0 - Argumentos passados corretamente e o programa corre normal.
    1 - Caminho não existe ou não é pasta
    2 - Argparse - Argumento inválido / Falta de Argumentos / Opções inválidas / Type Errors / etc
    3 - Problemas ao ler o ficheiro de configuração JSON
    101 - Opção unknown não encontrada