import unittest

from settings.arguments import ArgumentsParser


class ArgumentsParserTestCase(unittest.TestCase):

    base_args = 'site.org site-back.org'

    base_expected_result = {'server-name': 'site.org',
                            'proxy-pass': 'site-back.org'}

    ssl_args = ('--ssl-path /ssl/path --key /ssl/key --cert /ssl/cert'
                ' --trust-cert /ssl/trust')

    ssl_expected_result = {'ssl_path': '/ssl/path',
                           'key': '/ssl/key',
                           'trust_cert': '/ssl/trust'}

    file_args = '--output-file /file/out --output-symlink /file/link'

    file_expected_result = {'output_file': '/file/out',
                            'output_symlink': '/file/link'}

    def setUp(self):
        self.parser = ArgumentsParser(auto_parse=False)

    def merge_dicts(self, a, b):
        r = a.copy()
        r.update(b)
        return r

    def make_parse_test(self, args, expected_value):
        self.parser.parse(args.split())
        result = self.parser.get_all()
        result_keys = result.keys() & expected_value.keys()
        self.assertEqual({k: result[k] for k in result_keys},
                         expected_value)

    def test_use_ssl_args(self):
        command_args = self.base_args + ' --use-ssl ' + self.ssl_args

        expected_value = self.merge_dicts(self.base_expected_result,
                                          self.ssl_expected_result)
        expected_value['use_ssl'] = True

        self.make_parse_test(command_args, expected_value)

    def test_force_ssl_args(self):
        command_args = self.base_args + ' --force-ssl ' + self.ssl_args

        expected_value = self.merge_dicts(self.base_expected_result,
                                          self.ssl_expected_result)
        expected_value['force_ssl'] = True

        self.make_parse_test(command_args, expected_value)

    def test_output_file_args(self):
        command_args = self.base_args + ' ' + self.file_args

        expected_value = self.merge_dicts(self.base_expected_result,
                                          self.file_expected_result)
        expected_value['overwrite_output'] = None

        self.make_parse_test(command_args, expected_value)

    def test_output_file_overwrite_args(self):
        command_args = (self.base_args + ' --overwrite-output  '
                        + self.file_args)

        expected_value = self.merge_dicts(self.base_expected_result,
                                          self.file_expected_result)
        expected_value['overwrite_output'] = True

        self.make_parse_test(command_args, expected_value)

    def test_debug_arg(self):
        command_args = self.base_args + ' --debug'

        expected_value = self.merge_dicts({'debug': True},
                                          self.base_expected_result)

        self.make_parse_test(command_args, expected_value)
