import os.path

from jinja2 import Environment, PackageLoader
from settings.settings import Settings

class Render():
    def __init__(self, settings):
        self.settings = settings
        self.env = Environment(loader=PackageLoader('nginx-config',
                                                    'templates'))
        self.template = self.env.get_template('vhost.conf')
        self.content = self.template.render(settings.get_all())
        self.output_file = self.settings.get('output_file')

    def render(self):
        if self.output_file is not None:
            print('Writing output to ' + self.output_file)
            self.to_file()
        else:
            print(self.content)

    def to_file(self):
        if (os.path.isfile(self.output_file)
                and self.settings.get('overwrite_output') is not True):
                print('Output file aleready exists, use --overwrite-output'
                      ' to force')
                return
        try:
            f = open(self.output_file, 'w')
            f.write(self.content)
            f.close()
        except:
            print('Unable to write generated template to file')


