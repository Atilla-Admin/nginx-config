import os.path

from jinja2 import Environment, PackageLoader


class Render():
    def __init__(self, settings):
        self.settings = settings
        self.env = Environment(
                loader=PackageLoader(
                    'nginx-config',
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
        self.ensure_log_present()

    def to_file(self):
        print('Writing output to {}'.format(self.output_file))
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
        print('Creating symlink {}'.format(self.output_symlink))
        if (os.path.isfile(self.output_symlink)
                and self.settings.get('overwrite_output') is not True):
                print('File aleready exists, use --overwrite-output to force')
                return
        try:
            os.symlink(self.output_file, self.output_symlink)
        except:
            print('Unable to create the symbolic link')

    def ensure_log_present(self):
        if not os.path.exists(self.settings.get('log_path')):
            if self.settings.get('ensure_log_directory'):
                print('Creating the log directory')
                try:
                    os.makedirs(self.settings.get('log_path'))
                except:
                    print('Unable to create the log directory')
            else:
                print('Log directory not created, use --ensure-log-directory'
                      ' to create it')
