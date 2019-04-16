import pyautogui
from time import sleep
from tkinter import *


class AutomationSpotify:

    def __init__(self, spotify):
        frame = Frame(spotify)
        frame.pack()

        self.open_spotifyButton = Button(frame, text='Open Spotify', command=self.open_spotify, fg='white', bg='green',
                                         font='Proximanova 11 bold')
        self.open_spotifyButton.grid(row=0, padx=1, pady=1, sticky=W + E)

        self.close_spotifyButton = Button(frame, text='❌ Spotify', command=self.close_spotify, fg='white', bg='black',
                                          font='Proximanova 11 bold')
        self.close_spotifyButton.grid(row=0, column=4, padx=1, pady=1, sticky=W + E)

        self.search = Label(frame, text='Search:', fg='white', bd=1, bg='black', relief=SUNKEN, font='Proximanova 11 bo'
                                                                                                     'ld')
        self.search.grid(row=1, sticky=W + E)

        self.search_song = Entry(frame, font='Proximanova 11')
        self.search_song.grid(row=1, column=2)

        self.play_songButton = Button(frame, text='Play', command=self.play_song, fg='white', bg='green',
                                      font='Proximanova 11 bold')
        self.play_songButton.grid(row=1, column=4, padx=1, pady=1, sticky=W + E)

        self.next_songButton = Button(frame, text='⏭', command=self.next_song, fg='white', bg='black', font='Proximanov'
                                                                                                            'a 11')
        self.next_songButton.grid(row=2, column=4, padx=1, pady=1)

        self.play_pauseButton = Button(frame, text='⏯', command=self.play_pause, fg='white', bg='black', font='Proximan'
                                                                                                              'ova 11')
        self.play_pauseButton.grid(row=2, column=2, padx=1, pady=1)

        self.previous_songButton = Button(frame, text='⏮', command=self.previous_song, fg='white', bg='black',
                                          font='Proximanova 11')
        self.previous_songButton.grid(row=2, padx=1, pady=1)

        self.shuffle_songButton = Button(frame, text='Shuffle', command=self.shuffle_song, fg='white', bg='black',
                                         font='Proximanova 11 bold')
        self.shuffle_songButton.grid(row=3, column=4, padx=1, pady=1, sticky=W + E)

        self.repeat_songButton = Button(frame, text='Repeat', command=self.repeat_song, fg='white', bg='black', font='P'
                                                                                                'roximanova 11 bold')
        self.repeat_songButton.grid(row=4, column=4, padx=1, pady=1, sticky=W + E)

        self.add_to_queueButton = Button(frame, text='Queue', command=self.add_to_queue, fg='white', bg='black', font='Proximanova 11 bold')
        self.add_to_queueButton.grid(row=5, column=4, padx=1, pady=1, sticky=W + E)

        self.add_to_libraryButton = Button(frame, text='Save', command=self.add_to_library, fg='white', bg='green', font
        ='Proximanova 11 bold')

        self.add_to_libraryButton.grid(row=6, column=4, padx=1, pady=1, sticky=W + E)

        self.library_songButton = Button(frame, text='Songs', command=self.library_song, fg='white', bg='black',
                                         font='Proximanova 11 bold')
        self.library_songButton.grid(row=7, column=4, padx=1, pady=1, sticky=W + E)

    def open_spotify(self):
        # Clicks on search bar in Windows
        pyautogui.click(174, 1066)
        sleep(2)
        # Types in search bar
        pyautogui.typewrite('Spotify')
        sleep(2)
        # Clicks on Spotify icon
        pyautogui.click(144, 505)
        sleep(2)
        # Maximize Spotify window
        pyautogui.hotkey('alt', 'space')
        sleep(2)
        pyautogui.hotkey('x')
        sleep(2)

    def close_spotify(self):
        # Minimizes Spotify window
        pyautogui.click(599, 10)
        sleep(2)
        pyautogui.hotkey('alt', 'space')
        sleep(2)
        pyautogui.hotkey('r')
        sleep(2)
        # Closes Spotify window
        pyautogui.hotkey('alt', 'f4')
        sleep(2)

    def play_song(self):
        song_name = self.search_song.get()

        # Deletes everything in search bar
        pyautogui.click(599, 10)
        sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        sleep(2)
        pyautogui.hotkey('backspace')
        sleep(2)
        # Enters in a song name from user input
        pyautogui.typewrite(song_name)
        sleep(2)
        # Plays the first song in Spotify
        pyautogui.click(338, 238)
        sleep(2)

    def next_song(self):
        # Moves to the next song
        pyautogui.click(1005, 985)
        sleep(2)

    def play_pause(self):
        # Plays and pauses song
        pyautogui.click(957, 979)
        sleep(2)

    def previous_song(self):
        # Moves to the previous song
        pyautogui.click(908, 982)
        sleep(2)

    def shuffle_song(self):
        # Turns on shuffle
        pyautogui.click(861, 984)
        sleep(2)

    def repeat_song(self):
        # Turns on repeat
        pyautogui.click(1058, 984)
        sleep(2)

    def add_to_queue(self):
        song_name = self.search_song.get()

        # Deletes everything in search bar
        pyautogui.click(599, 10)
        sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        sleep(2)
        pyautogui.hotkey('backspace')
        sleep(2)
        # Enters in a song name from user input
        pyautogui.typewrite(song_name)
        sleep(2)
        # Adds song to queue
        pyautogui.rightClick(338, 238)
        sleep(2)
        pyautogui.click(366, 259)
        sleep(2)

    def add_to_library(self):
        # Saves song to library
        pyautogui.rightClick(338, 238)
        sleep(2)
        pyautogui.click(489, 440)
        sleep(2)

    def library_song(self):
        # Opens personal library
        pyautogui.click(47, 295)
        sleep(2)
        # Plays song in library
        pyautogui.click(248, 302)
        sleep(2)


root = Tk()
system = AutomationSpotify(root)
root.title('Spotify Script')
root.configure(bg='black')
root.mainloop()
