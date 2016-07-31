import os.path

from jinja2 import Environment, PackageLoader


class Render():
    def __init__(self, settings):
        self.settings = settings
        self.env = Environment(loader=PackageLoader('nginx-config',
                                                    'templates'))
        self.template = self.env.get_template('vhost.conf')
        self.content = self.template.render(settings.get_all())

        """ Load options that we'll use frequently """
        self.output_file = self.settings.get('output_file')
        self.output_symlink = self.settings.get('output_symlink')

    def render(self):
        if self.output_file is not None:
            self.to_file()
        else:
            print(self.content)

    def to_file(self):
        print('Writing output to ' + self.output_file)
        if (os.path.isfile(self.output_file)
                and self.settings.get('overwrite_output') is not True):
                print('Output file aleready exists, use --overwrite-output'
                      ' to force')
                return
        try:
            f = open(self.output_file, 'w')
            f.write(self.content)
            f.close()
            if self.output_symlink is not None:
                self.create_symlink()
        except:
            print('Unable to write generated template to file')

    def create_symlink(self):
        print('Creating symlink ' + self.output_symlink)
        if (os.path.isfile(self.output_symlink)
                and self.settings.get('overwrite_output') is not True):
                print('File aleready exists, use --overwrite-output to force')
                return
        try:
            os.symlink(self.output_file, self.output_symlink)
        except:
            print('Unable to create the symbolic link')
