# 8-7

def make_album(artist_name, album_title, number_of_tracks = ''):
    """Return a dictionary"""
    album = {'Artist': artist_name, 'Title': album_title, 'No of Tracks': number_of_tracks}
    return album

album_one = make_album('Sunken Physics', 'Food of the Many Summer')
album_two = make_album('Apprentice Hindsight', 'Red Bypass', number_of_tracks = 9)
album_three = make_album('Realist Twinkie', 'Rhubarb Goat')

print(album_one)
print(album_two)
print(album_three)