# Music Player & Playlist Scheduler
'''
Covering topics - OOPs (class , properties, dunder methods) , Time formatting

TASKS:
●	Create Track(title, artist, duration) — parse duration string 'mm:ss' and store as integer seconds internally
●	Add a formatted_duration property that converts seconds back to 'mm:ss'; implement __str__ as 'Title by Artist [mm:ss]'
●	Create Playlist(name) with add(track), remove(track), and total_duration() returning the sum as a formatted 'mm:ss' string
●	Add longest_track(), shortest_track(), average_duration(), tracks_under(seconds), and a summary() method that prints all stats

Hint:
Parse 'mm:ss' → int(m)*60 + int(s). Format back → f'{s//60}:{s%60:02d}'. Use max(self.tracks, key=lambda t: t.seconds) for longest. Average = total_seconds // len, then format.
'''

class Track:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.time = duration.split(":")
        self.min = int(self.time[0])
        self.sec = int(self.time[1])
        self.total_seconds = self.min * 60 +self.sec

    def formatted_duration(self):
        return f"{self.total_seconds//60}:{self.total_seconds%60:02d}"

    def __str__(self):
        return f"{self.title} by {self.artist} [{self.formatted_duration()}]"
    
class Playlist:
    def __init__(self,name):
        self.name = name
        self.track_list = []

    def add(self,track):
        self.track_list.append(track)

    def remove(self,track):
        for song in self.track_list:
            if song.title == track.title:
                self.track_list.remove(song)
                break

    def total_duration(self):
        total = 0
        for song in self.track_list:
            total += song.total_seconds
        return f"{total//60}:{total%60:02d}"

    def tracks_under(self,time_seconds):
        if not self.track_list:
            return "No song in playlist"
        result_list = []
        for t in track_list:
            if t.total_seconds < 200:
                result_list.append(t.title)
        return result_list

    def longest_track(self):
        if not self.track_list:
            return "No Song in playlist"
        longest = self.track_list[0]
        for t in track_list:
            if t.total_seconds > longest.total_seconds:
                longest = t
        
        return longest
        
    
    def shortest_track(self):
        if not self.track_list:
            return "No Song in playlist"
        shortest = self.track_list[0]
        for t in track_list:
            if t.total_seconds < shortest.total_seconds:
                shortest = t
        
        return shortest
        

    def format_seconds(self,seconds):
        return f"{seconds//60}:{seconds%60:02d}"

    def average_duration(self):
        if not self.track_list:
            return "0:00"
        total_seconds = sum(t.total_seconds for t in track_list)
        average_seconds = total_seconds // len(self.track_list)

        return f"{self.format_seconds(average_seconds)}"

    def summary(self):
        print(f"{self.name} | {len(track_list)} tracks | Total :{self.total_duration()} | Avg : {self.average_duration()}")

    

# Input
track_list = [
  Track("Blinding Lights", "The Weeknd", "3:20"),
  Track("Levitating", "Dua Lipa", "3:23"),
  Track("Stay", "Kid LAROI", "2:21"),
  Track("Peaches", "Justin Bieber", "3:18"),
  Track("Good 4 U", "Olivia Rodrigo", "2:58"),
]

playlist = Playlist("Evening Vibes")
for t in track_list:
    playlist.add(t)

# for output :--

print(track_list[0])
print(track_list[0].total_seconds)
print(playlist.total_duration())
print(playlist.longest_track())
print(playlist.shortest_track())
print(playlist.tracks_under(200))
print(playlist.average_duration())
playlist.summary()