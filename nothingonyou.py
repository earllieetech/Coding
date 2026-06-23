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
        ("\n""Beautiful girls", 0.09),
        ("All over the world", 0.09),
        ("I could be chasing, But my time", 0.09),
        ("Would be wasted", 0.08),
        ("They got nothing on you, baby", 0.08),
        ("Nothing on you, baby", 0.12),

    ]
    delays = [0.3, 2.8, 5.6, 8.6, 9.8, 14.0]

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