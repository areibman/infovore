class FileReader:
    def __init__(self):
        pass

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            file_content = file.read()
        return file_content
