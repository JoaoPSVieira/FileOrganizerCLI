class Report:
    def __init__(self):
        self.analized_files = 0
        self.moved_copied_files = 0
        self.ignored_files = 0
        self.errors = 0
        self.files_per_category = {}
        self.mode = ""
    
    def moved_or_copied(self, mode):
        self.mode = "movidos" if mode == "move" else self.mode == "copiados"

    def increase_analized_files(self):
        self.analized_files += 1

    def print_files_per_category(self):
        result = ""
        for categoria, quantidade in self.files_per_category.items():
            result += f"{categoria} -> {quantidade} ficheiros\n"
        return result
    
    def print_all(self):
        print(f"""
            Nº total de ficheiros analizados: {self.analized_files}
            Nº total de ficheiros {self.mode}: {self.moved_copied_files}
            Nº total de ficheiros ignorados: {self.ignored_files}
            Nº de erros: {self.errors}
            Contagem por categoria:
                {self.print_files_per_category()}
        """)