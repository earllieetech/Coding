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
        ("\nRemember when I told you", 0.07),
        ("No matter where I go", 0.09),
        ("I'll never leave your side", 0.08),
        ("You will never be alone", 0.09),
        ("\nEven when we go through changes", 0.07),
        ("Even when we're old", 0.08),
        ("Remember that I told you", 0.08),
        ("I'll find my way back home", 0.08),
        
    ]
    delays = [0.3, 2.5, 5.6, 7.8, 10.0, 13.0, 14.2, 15.0]
    
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