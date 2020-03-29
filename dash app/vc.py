import vlc
import time

a = input("Value : ")
if a <= 18:
    sf1 = vlc.MediaPlayer("/home/vimal/Vimal/dash app/tmpc.mp3")
    sf1.play()
    time.sleep(5)
elif a <= 35:
    sf2 = vlc.MediaPlayer("/home/vimal/Vimal/dash app/tmpn.mp3")
    sf2.play()
    time.sleep(5)
elif a >= 35:
    sf3 = vlc.MediaPlayer("/home/vimal/Vimal/dash app/tmph.mp3")
    sf3.play()
    time.sleep(5)
