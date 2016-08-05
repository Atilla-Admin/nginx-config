import argparse


class ArgumentsParser():

    description = """ Generate and activate a new Nginx vhost file for a
                      reverse-proxy configuration."""

    epilog = ""

    def __init__(self, auto_parse=True):
        self.parser = argparse.ArgumentParser(description=self.description,
                                              epilog=self.epilog)

        self.ssl_group = self.parser.add_argument_group(title='SSL')

        self.ssl_method = self.ssl_group.add_mutually_exclusive_group()

        self.parser.add_argument('server-name', help='new server name')

        self.parser.add_argument('proxy-pass', help='proxy pass address')

        self.ssl_method.add_argument('--use-ssl', '-us',
                                     help='activate SSL support',
                                     action='store_true',
                                     default=None,
                                     dest='use_ssl')

        self.ssl_method.add_argument('--force-ssl', '-fs',
                                     help='force SSL support',
                                     action='store_true',
                                     default=None,
                                     dest='force_ssl')

        self.ssl_group.add_argument('--ssl-path',
                                    help=('path in which SSL '
                                          'files can be found'),
                                    dest='ssl_path')

        self.ssl_group.add_argument('--key',
                                    help='SSL certificate key file name')

        self.ssl_group.add_argument('--cert',
                                    help='SSL fullchain certificate')

        self.ssl_group.add_argument('--trust-cert',
                                    help='SSL trusted certificate',
                                    dest='trust_cert')

        self.parser.add_argument('--debug', '-d',
                                 help='enable debug mode in error logs',
                                 default=None,
                                 action='store_true')

        self.parser.add_argument('--log-path',
                                 help='log path',
                                 dest='log_path')

        self.parser.add_argument('--ensure-log-directory',
                                 help='ensure that the log dir is present',
                                 action='store_true',
                                 dest='ensure_log_directory')

        self.parser.add_argument('--output-file',
                                 help='output file',
                                 dest='output_file')

        self.parser.add_argument('--output-symlink',
                                 help='symlink to output file',
                                 dest='output_symlink')

        self.parser.add_argument('--overwrite-output',
                                 help=('owerwrite the output file if it '
                                       'already exists'),
                                 default=None,
                                 action='store_true',
                                 dest='overwrite_output')

        if auto_parse:
            self.parse()

    def parse(self, args=None):
        self.args = self.parser.parse_args(args)

    def help(self):
        return self.parser.print_help()

    def get_all(self):
        return vars(self.args)

    def get_arg(self, arg):
        return vars(self.args)[arg]
