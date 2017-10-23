from __future__ import absolute_import

try:
    import dotenv
except ImportError:  # pragma: no cover
    dotenv = None


class DotenvBackend(object):

    def __init__(self, dotenv_path):
        if dotenv is None:
            raise ImportError('install configstore[dotenv] to use '
                              'the dotenv backend')

        with open(dotenv_path) as file:
            content = file.read()

        self.config = dotenv.parse_dotenv(content)

    def get_setting(self, key):
        return self.config.get(key)