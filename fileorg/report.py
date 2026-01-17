class Report:
    def __init__(self):
        self.analized_files = 0
        self.moved_copied_files = 0
        self.ignored_files = 0
        self.errors = 0
        self.files_per_category = {}
    
    def increase_analized_files(self):
        self.analized_files += 1
    
    def print_all(self):
        print("Ficha:", self.analized_files)