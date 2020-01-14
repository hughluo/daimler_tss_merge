"""
User-defined class Error.
"""
__author__ = "Yinchi Wexort Luo"
__email__ = "yinchi.luo@gmail.com"


class Error(Exception):
    pass


class InputError(Error):

    def __init__(self, message):
        self.message = message
