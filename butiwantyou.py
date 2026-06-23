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
        ("\nOoh, you're just my type", 0.07),
        ("Everything's so right", 0.09),
        ("And I just wanna chill", 0.08),
        ("So, let's dip up out of here", 0.09),
        ("Let's dip up out of here, (here)", 0.07),
        ("aahh", 0.19,),
        ("She's fine too", 0.14),
        ("But I want you >_<", 0.16),
        
    ]
    delays = [0.3, 2.5, 5.6, 7.8, 10.0, 13.3, 16.0, 19.2]
    
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