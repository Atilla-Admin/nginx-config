import configparser


class FileParser():
    def __init__(self, file_name='settings.ini'):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(file_name)
        self.config = dict(vars(self.config_parser)['_sections']['General'])

    def get_arg(self, arg):
        return self.config[arg]

    def get_all(self):
        return self.config
