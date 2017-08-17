import os.path
import re

from imhotep.tools import Tool

class ESLint(Tool):
    # Example: foo.js: line 5, col 3, Operator + should not stick ...etc
    response_format = re.compile(r'^(?P<filename>.*): ' \
        r'line (?P<line_number>\d+), col \d+, (?P<message>.*)$')
    file_extensions = ('.js', '.jsx')

    def get_command(self, dirname, linter_configs=None):
        return 'eslint -f compact'
