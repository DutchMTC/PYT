import webbrowser
import time

x = 1000
while x > 0:
    print(x)
    time.sleep(0.02)
    x = x - 1

if x == 0:
    print(0)
    time.sleep(1)
    print("\nThanks for waiting. Enjoy getting Rick Rolled!")
    time.sleep(2)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')