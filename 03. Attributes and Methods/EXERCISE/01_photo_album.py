from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f'{label} photo added successfully on page {i + 1} slot {self.photos[i].index(label) + 1}'
        return 'No more free spots'

    def display(self):
        result = f'{"-" * 11}\n'
        for page in self.photos:
            for _ in page:
                result += '[] '
            if result[-1] != '\n':
                result = result.rstrip()
            result += f'\n{"-" * 11}\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
