import keyboard

def get_numbers():
    nummer = ""
    keypress0 = False
    keypress1 = False
    keypress2 = False
    keypress3 = False
    keypress4 = False
    keypress5 = False
    keypress6 = False
    keypress7 = False
    keypress8 = False
    keypress9 = False
    while True:
        
        if not keyboard.is_pressed("0") and keypress0:
            nummer += "0"
        if keyboard.is_pressed("0") and not keypress0:
            keypress0 = True
            
        if not keyboard.is_pressed("1") and keypress1:
            nummer += "1"
        if keyboard.is_pressed("1") and not keypress1:
            keypress1 = True
            
        if not keyboard.is_pressed("2") and keypress2:
            nummer += "2"
        if keyboard.is_pressed("2") and not keypress2:
            keypress2 = True
        
        if not keyboard.is_pressed("3") and keypress3:
            nummer += "3"
            keypress3 = False
        if keyboard.is_pressed("3") and not keypress3:
            keypress3 = True
        
        if not keyboard.is_pressed("4") and keypress4:
            nummer += "4"
        if keyboard.is_pressed("4") and not keypress4:
            keypress4 = True
        
        if not keyboard.is_pressed("5") and keypress5:
            nummer += "5"
        if keyboard.is_pressed("5") and not keypress5:
            keypress5 = True
        
        """if keyboard.on_release("6"):
            nummer += "6"
        if keyboard.on_release("7"):
            nummer += "7"
        if keyboard.on_release("8"):
            nummer += "8"
        if keyboard.on_release("9"):
            nummer += "9"""
            
        if keyboard.is_pressed("enter"):
            return nummer


while True:
    print(get_numbers())
