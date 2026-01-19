def string_box(texto):
    largura = len(texto) + 4
    print("\n", "\t" * 2, "*" * largura)
    print(f"{"\t" * 2} * {texto} *")
    print("\t" * 2, "*" * largura)

class Report:
    def __init__(self):
        self.analized_files = 0
        self.moved_copied_files = 0
        self.ignored_files = 0
        self.errors = 0
        self.files_per_category = {}
        self.mode = ""
    
    def moved_or_copied(self, mode):
        self.mode = "movidos" if mode == "move" else "copiados"

    def increase_analized_files(self):
        self.analized_files += 1

    def moved_or_copied_files(self):
        self.moved_copied_files += 1
    
    def increase_ignored_files(self):
        self.ignored_files += 1
    
    def increase_errors(self):
        self.errors += 1

    def add_category_files(self, category):
        if category not in self.files_per_category.keys():
            self.files_per_category[category] = 0
        self.files_per_category[category] += 1

    def print_files_per_category(self):
        result = ""
        for categoria, quantidade in sorted(self.files_per_category.items(), key=lambda item: item[1], reverse=True):
            result += f"\t\t{categoria} -> {quantidade} ficheiros\n"
        return result
    
    def print_all(self, dry_run):
        if dry_run: string_box("SIMULAÇÃO")

        print(f"""
        • Nº total de ficheiros analizados: {self.analized_files}
        • Nº total de ficheiros {self.mode}: {self.moved_copied_files}
        • Nº total de ficheiros ignorados: {self.ignored_files}
        • Nº de erros: {self.errors}
        • Contagem por categoria:""")
        print(f"{self.print_files_per_category()}")