# 8-8

def make_album(artist_name, album_title, number_of_tracks):
    """Return a dictionary"""
    album = {'Artist': artist_name, 'Title': album_title, 'No of Tracks': number_of_tracks}
    return album

while True:
    print("\nEnter artist name, and album title, and number of tracks: ")
    print("(enter 'q' to to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break

    num_of_tracks = input("No. of tracks: ")
    if num_of_tracks == 'q':
        break

    album = make_album(a_name, a_title, num_of_tracks)

    print(album)