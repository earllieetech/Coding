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
        ("\n\"Ikaw ang tangi kong iniibig", 0.14),
        ("Ikaw ang aking mahal", 0.09),
        ("Magpakailanman", 0.11),
        ("Dito sa aking puso", 0.15),
    ]

    delays = [0.3, 6.0, 9.3, 11.8]

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