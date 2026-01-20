import json

# Definição das regras padrão em caso de não especificação por parte do utilizador
DEFAULT_RULES = {
    "Imagens": [".jpg", "jpeg", "png", "gif", "webp"],
    "Documentos": ["pdf", "docx", "txt", "md"],
    "Compactados": ["zip", "rar", "7z", "tar", "gz"],
    "Audio": ["mp3", "wav", "flac"],
    "Vídeo": ["mp4", "mkv", "avi"],
    "Código": ["py", "cpp", "java", "html", "css", "js"],
    "Other": []
}

# Escolhe entre a configuração padrão ou a escolhida pelo utilizador
def load_config(path=None):
    if path:
        with open(path, "r") as f:
            return invert_rules(json.load(f))
    return invert_rules(DEFAULT_RULES)

# Inverte as regras para aumentar a eficiencia durante a organização dos ficheiros
def invert_rules(rules):
    extension_map = {}

    for category, extensions in rules.items():
        for ext in extensions:
            # Se tiver um ponto irá ser removido e se tiver letras maiúsculas irá ser trocado por letras minúsculas
            if (ext[0] == "." or ext.isupper()):
                extension_map[ext[1:].lower()] = category
            else:
                extension_map[ext] = category
    return extension_map