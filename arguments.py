import argparse

class ArgumentsParser():

    description = """ Generate and activate a new Nginx vhost file for a
                      reverse-proxy configuration."""

    epilog = ""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.description,
                                              epilog=self.epilog)

        self.ssl_group = self.parser.add_argument_group(title='SSL')

        self.ssl_method = self.ssl_group.add_mutually_exclusive_group()

        self.parser.add_argument('server-name', help='new server name')

        self.parser.add_argument('proxy-pass', help='proxy pass address')

        self.ssl_method.add_argument('--use-ssl', '-us',
                                     help='activate SSL support',
                                     action='store_true')

        self.ssl_method.add_argument('--force-ssl', '-fs',
                                     help='force SSL support',
                                     action='store_true')

        self.ssl_group.add_argument('--ssl-path',
                                    help=('path in which SSL '
                                          'files can be found'))

        self.ssl_group.add_argument('--key',
                                 help='SSL certificate key file name')

        self.ssl_group.add_argument('--cert',
                         help='SSL fullchain certificate')

        self.ssl_group.add_argument('--trust-cert',
                                 help='SSL trusted certificate')

        self.parser.add_argument('--debug', '-d',
                                 help='enable debug mode in error logs',
                                 action='store_true')

        self.parser.add_argument('--log-path',
                                 help='log path')

        self.parse()

    def parse(self):
        self.args = self.parser.parse_args()
        print(vars(self.args))

    def help(self):
        return self.parser.print_help()

    def get_all(self):
        return vars(self.args)

    def get_arg(self, arg):
        return vars(self.args)[arg]
