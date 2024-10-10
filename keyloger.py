import pynput.keyboard


def dinle(harfler):
    global toplama
    toplama= ""
    toplama +=str(harfler)
    print(toplama)
    
dinleme =pynput.keyboard.Listener(on_press=dinle)


with dinleme:
    dinleme.join()
    