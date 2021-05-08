from storages.json import JsonStorage
from storages.text import TextStorage


class StorageFactory(object):

    @staticmethod
    def factory(extension):
        mapping = {
            'dat': JsonStorage,
            'data': TextStorage
        }
        return mapping.get(extension, TextStorage)
