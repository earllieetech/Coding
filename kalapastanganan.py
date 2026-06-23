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
        ("\noh, oohhhh", 0.47),
        ("Mamamatay akong nakangiti", 0.12),
        ("Kapag ikaw ang nasa aking tabi", 0.13),
        ("Mabubuhay akong nagsisisi", 0.13),
        ("Kapag isang araw hindi ka mapangiti", 0.13),
        ("Kalapastangan ang di ka ibigin", 0.12),
        ("Kalokohan ang di ka isipin", 0.12),
        ("Kung ang mundo ay biglang gugunawin", 0.11),
        ("Ikaw ang una kong hahanapin", 0.12),
    ]

    delays = [0.3, 9.5, 13.3, 17.7, 21.8, 26.9, 31.2, 35.7, 39.9]

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