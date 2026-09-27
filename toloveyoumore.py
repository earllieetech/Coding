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
        ("\n""All the things", 0.07),
        ("That your heart", 0.08),
        ("Needs to know", 0.10),
        ("I'll be...", 0.10),
        ("Waiting for you", 0.13),
        ("Here inside my heart", 0.10),
        ("I'm the one who wants to", 0.12),
        ("Love you more", 0.15),
    ]
    
    delays = [0.3, 2.2, 4.0, 8.0, 10.2, 14.4, 17.0, 20.0]
    
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