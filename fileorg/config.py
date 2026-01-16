import json

# Definição das regras padrão em caso de não especificação por parte do utilizador
DEFAULT_RULES = {
    "Imagens": ["jpg", "jpeg", "png", "gif", "webp"],
    "Documentos": ["pdf", "docx", "txt", "md"],
    "Compactados": ["zip", "rar", "7z", "tar", "gz"],
    "Audio": ["mp3", "wav", "flac"],
    "Vídeo": ["mp4", "mkv", "avi"],
    "Código": ["py", "cpp", "java", "html", "css", "js"],
    "Other": []
}

def load_config(path=None):
    if path:
        with open(path, "r") as f:
            return json.load(f)
    return DEFAULT_RULES