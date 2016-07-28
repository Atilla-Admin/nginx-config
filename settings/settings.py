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

        self.settings['server-name'] = self.arguments['server-name']
        self.settings['proxy-pass'] = self.arguments['proxy-pass']

        """ The configuration file should contain every configuration
            directives """
        for key in self.file_config:
            if ((key in self.arguments)
                    and (self.arguments[key] is not None)):
                self.settings[key] = self.arguments[key]
            elif self.file_config[key] == 'yes':
                self.settings[key] = True
            elif self.file_config[key] == 'no':
                self.settings[key] = False
            else:
                self.settings[key] = self.file_config[key]

    """ Check if the final configuration is valid """
    def verify_configuration(self):
        if ((self.settings['use-ssl'] or self.settings['force-ssl'])
                and (self.settings['key'] is None
                        or self.settings['cert'] is None
                        or self.settings['trust-cert'] is None
                        or self.settings['ssl-path'] is None)):
            raise EnvironmentError("Bad configuration")

    def replace_keywords(self):
        for key in self.settings:
            if isinstance(self.settings[key], str):
                self.settings[key] = re.sub(r"\$server-name",
                                            self.settings['server-name'],
                                            self.settings[key])
                self.settings[key] = re.sub(r"\$proxy-pass",
                                            self.settings['proxy-pass'],
                                            self.settings[key])

    def get(self, arg):
        return self.settings[arg]
