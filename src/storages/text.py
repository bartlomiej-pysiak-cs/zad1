from storages.base import BaseStorage


class TextStorage(BaseStorage):
    EXTENSION = 'txt'

    @staticmethod
    def peform_save(file=None, data=None):
        file.write(data)
