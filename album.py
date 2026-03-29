# album

def album(title, artist, songs=None):
    """Enter the details of a music album"""    
    if songs:
        print(f"\n{title.title()} by {artist.title()} has {songs} songs.")
    else:
        print(f"{title.title()} by {artist.title()}")

album(
    title='Heavy Deeds',
    artist='Sun Araw',
    songs=5
)

album(
    title='Sun Ark Edit Bay #1',
    artist='Aristocrat P. Child',
    songs=4
)

album(
    title='The Phynx',
    artist='Sun Araw',
    songs=4
)

title = ""
artist = ""
songs = ""
def album_input(title, artist, songs=None):
    """Enter the details of a music album"""
    def quit(var):
        if var == 'q':
            exit
    while title != 'q' and artist != 'q' and songs != 'q':
        
        quit(var=title)
        quit(var=artist)   
        quit(var=songs)
        
        songs = int(songs)
        if songs:
            print(f"\n{title} by {artist} has {songs} songs.\n")
        else:
            print(f"\n{title} by {artist}.\n")
        
        print("Enter the details about a music album.\n")
        print("Enter 'q' to exit at any time.\n")
        title = input("Enter the album's title: ")
        artist = input("\nEnter the album artist: ")
        songs = input("\nEnter the number of songs on the album. (Optional): ")


album_input(
    title=input(
        "\nEnter the name of the album: "
    ),
    artist=input(
        "\nEnter the album artist: "
    ),
    songs=input(
        "\nEnter the number of songs on the album. (Optional): "
    )
)