class FileParser():
    def __init__(self, file_name='settings.ini'):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(file_name)
        self.configuration = self.config_parser['General']

    def get_arg(self, arg):
        return self.configuration[arg]

    def get_all(self):
        return self.configuration
