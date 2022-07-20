"""
TODO: add custom attribute to the exception
"""


class FHUException(Exception):
    pass


class PreUploadError(FHUException):
    pass


class MidUploadError(FHUException):
    pass


class PostUploadError(FHUException):
    pass


class DownloadError(FHUException):
    pass
