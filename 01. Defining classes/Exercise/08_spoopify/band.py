from .album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        else:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        for i in range(len(self.albums)):
            if album_name == self.albums[i].name:
                if self.albums[i].published:
                    return 'Album has been published. It cannot be removed.'
                else:
                    self.albums.remove(self.albums[i])
                    return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        return f'Band {self.name}\n' + '\n'.join([album.details() for album in self.albums])
   