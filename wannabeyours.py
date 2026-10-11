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
        ("\n""Maybe I just wanna be yours", 0.11),
        ("I wanna be yours", 0.11),
        ("I wanna be yours", 0.14),
        ("Wanna be yours", 0.14),
        ("Wanna be yours", 0.15),
        ("Wanna be yours...", 0.17),
    ]
    
    delays = [0.3, 3.2, 5.0, 9.0, 12.2, 15.6]
    
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