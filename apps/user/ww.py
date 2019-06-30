from django.core.files.storage import Storage


class FastDFSStorage(Storage):
    def url(self, name):
        return '/static/images/' + name