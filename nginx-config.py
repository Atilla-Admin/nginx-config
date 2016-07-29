from jinja2 import Environment, PackageLoader
from settings.settings import Settings

if __name__ == "__main__":
    settings = Settings()
    env = Environment(loader=PackageLoader('nginx-config', 'templates'))
    template = env.get_template('vhost.conf')
    print(template.render(settings.get_all()))
