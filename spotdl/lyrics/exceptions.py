class LyricsNotFoundError(Exception):
    __module__ = Exception.__module__

    def __init__(self, message=None):
        super(LyricsNotFoundError, self).__init__(message)
