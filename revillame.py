import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""Pwedeng sabihin n'yo 'to sa kanya?", 0.07),
        ("Ang puso ko'y nahihirapan na", 0.09),
        ("Ano pa ba ang pwede kong gawin", 0.09),
        ("Na uubra upang maakit siya?", 0.11),
        ("Palagay kaya ako ng tattoo", 0.11),
        ("Magpatubo ng balbas sa nguso", 0.12),
        ("Magpalaki ng masel sa braso", 0.10),
        ("Magpadagdag ng pwet kay beloooooo", 0.12),
        ("Buksan mo, papasukin ako, (papasukin ako)", 0.11),
        ("Bulaklak para sa'yo", 0.11),
        ("ano ba'ng, gusto mong gawin ko", 0.10),
        ("Para mahalin mo?", 0.11),
        
    ]
    delays = [0.3, 3.5, 6.6, 9.8, 14.0, 18.0, 22.2, 26.9, 30.0, 34.1, 38.3, 41.8]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
