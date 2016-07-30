import re

from .arguments import ArgumentsParser
from .files import FileParser

class Settings():
    def __init__(self):
        self.arguments = ArgumentsParser().get_all()
        self.file_config = FileParser().get_all()
        self.merge_configurations()
        self.verify_configuration()
        self.replace_keywords()

    def merge_configurations(self):
        self.settings = {}

        self.settings['server_name'] = self.arguments['server-name']
        self.settings['proxy_pass'] = self.arguments['proxy-pass']

        """ The configuration file should contain every configuration
            directives """
        for key in self.file_config:
            if ((key in self.arguments)
                    and (self.arguments[key] is not None)):
                self.settings[key] = self.arguments[key]
            elif "yes" == self.file_config[key]:
                self.settings[key] = True
            elif "no" == self.file_config[key]:
                self.settings[key] = False
            else:
                self.settings[key] = self.file_config[key]

    """ Check if the final configuration is valid """
    def verify_configuration(self):
        if ((self.settings['use_ssl'] or self.settings['force_ssl'])
                and (self.settings['key'] is None
                        or self.settings['cert'] is None
                        or self.settings['trust_cert'] is None
                        or self.settings['ssl_path'] is None)):
            raise EnvironmentError("Bad configuration")

    def replace_keywords(self):
        for key in self.settings:
            if isinstance(self.settings[key], str):
                self.settings[key] = re.sub(r"\$server_name",
                                            self.settings['server_name'],
                                            self.settings[key])
                self.settings[key] = re.sub(r"\$proxy_pass",
                                            self.settings['proxy_pass'],
                                            self.settings[key])

    def get_all(self):
        return self.settings

    def get(self, arg):
        if arg not in self.settings:
            return None
        return self.settings[arg]
