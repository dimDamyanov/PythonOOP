from .song import Song


class Album:
    def __init__(self, name: str, *args: Song):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        elif self.published:
            return f'Cannot add songs. Album is published.'
        elif song in self.songs:
            return f'Song is already in the album.'
        else:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        for i in range(len(self.songs)):
            if song_name == self.songs[i].name:
                if self.published:
                    return 'Cannot remove songs. Album is published.'
                else:
                    self.songs.remove(self.songs[i])
                    return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        else:
            self.published = True
            return f'Album {self.name} has been published.'

    def details(self):
        return f'Album {self.name}\n' + ''.join([f'== {song.get_info()}\n' for song in self.songs])
