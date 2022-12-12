from ChainingHashTableMap import ChainingHashTableMap as map

class PlayList:
    def __init__(self):
        self.playlist = map()
        self.num_songs = 0
    
    def add_song(self,new_song_name):
        self.num_songs += 1
        self.playlist[new_song_name] = self.num_songs
        

    def add_song_after(self,song_name, new_song_name):
        if not song_name in self.playlist:
            raise KeyError("Song not in playlist")
        self.playlist[new_song_name] = self.playlist[song_name] + 1
        self.num_songs += 1
    
    def play_song(self,song_name):
        if not song_name in self.playlist:
            raise KeyError("Song not in playlist")
        print("Playing " + song_name)
    
    def play_list(self):
        sequence = []
        for key in self.playlist:
            sequence.insert(self.playlist[key] - 1, key)
        
        for i in range(len(sequence)):
            print("Playing " + sequence[i])
        


        



def main():
    p1 = PlayList()
    p1.add_song("Jana Gana Mana")
    p1.add_song("Kimi Ga Yo")
    p1.add_song("The Star-Spangled Banner")
    p1.add_song("March of the Volunteers")
    p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
    p1.add_song_after("Kimi Ga Yo", "Aegukga")
    p1.add_song("Arise, O Compatriots")
    p1.add_song("Chant de Ralliement")
    p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
    p1.add_song_after("Jana Gana Mana", "God Save The Queen")

    p1.play_song("The Star-Spangled Banner")
    p1.play_song("Jana Gana Mana")

    p1.play_list( )

if __name__ == "__main__":
    main()