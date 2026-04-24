# Creating a system that allow user to manage a small library of songs and create a custom playlist
# class for a single song 
class Song:
    # title = name of song , artist = singer name , duration = length of song in minutes
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    # display the information of song
    def display_info(self):
        return f"Song: {self.title} by {self.artist} -- {self.duration} mins"

#class MusicLibrary for Home page of our jukebox
class MusicLibrary:
    def __init__(self):
        self.all_songs = []
    # method to add song object to library
    def add_to_library(self,song_obj):
        self.all_songs.append(song_obj)
    #method to list all songs in Music library
    def list_all_songs(self):
        for song in self.all_songs:
            print(song.display_info())

# class Playlist for user's custom playlist(set of songs)
class Playlist:
    # user's custom playlist name initialization
    def __init__(self,playlist_name):
        self.playlist_name = playlist_name
        self.my_songs = []
    # method to add song in playlist
    def add_songs(self,song):
        self.my_songs.append(song)
    #method to show total time duration of the playlist
    def show_total_time(self):
        total_duration = 0
        for song in self.my_songs:
            total_duration += song.duration
        return f"Total duration of songs: {total_duration}"

# Main App or System
library_obj = MusicLibrary() # Home page 

print("----- Welcome to jukebox -----\n")

# Different song objects
song1 = Song("Zaalima (Raees)","Arijit singh , Harshdeep Kaur",4.59)
song2 = Song("Bairan","Banjaare",2.30)
song3 = Song("Birds of a Feather","Billie Eilish",3.30)
song4 = Song("At Last","Etta James",3.00)

# adding to Library
library_obj.add_to_library(song1)
library_obj.add_to_library(song2)
library_obj.add_to_library(song3)
library_obj.add_to_library(song4)

print("All songs ---")
library_obj.list_all_songs()
print()

#creating my playlist
my_playlist = Playlist("Soothing") #playlist name in parameter
#adding songs
my_playlist.add_songs(song1) 
my_playlist.add_songs(song2)

print("My playlist ---\n")
print(f"-- : {my_playlist.playlist_name} : --\n")
for song in my_playlist.my_songs:
    print(song.display_info())
print(my_playlist.show_total_time())