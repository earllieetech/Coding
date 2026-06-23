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
        ("\n""Nandito ako", 0.32),
        ("Umiibig sa'yo", 0.19),
        ("Kahit na nagdurugo", 0.17),
        ("Ang puso", 0.18),
        ("At kung sakaling", 0.14),
        ("Iwanan ka niya", 0.17),
        ("'Wag kang mag-alala", 0.14),
        ("May nagmamahal sa'yo", 0.15),
        ("Nandito ako...", 0.16),
    ]

    delays = [0.3, 5.9, 8.9, 13.6, 16.3, 19.8, 23.9, 27.2, 30.6]

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