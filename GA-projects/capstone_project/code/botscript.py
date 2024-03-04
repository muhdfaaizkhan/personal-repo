import numpy as np
from windowcapture import WindowCapture
from model_class import CNN
import time
import keyboard as kb
from torch import load, tensor, no_grad
import capstone_library as cl
import pyKey as pk

# Initialise and load pre-trained CNN models
models = {}
for mon in cl.opponents:
    models[mon] = CNN()
    models[mon].load_state_dict(load('../model/{}.pth'.format(mon)))
    models[mon].eval()

# Initialise WindowCapture
wincap = WindowCapture('pkmncc_09')
portcap = WindowCapture('pkmncc_09',portrait=True)

def modelpredict(model, img):
    X = np.float32(np.array(img/255.0))
    X = np.expand_dims(X, axis=0)
    X = tensor(X).permute(0, 3, 1, 2)
    with no_grad():
        output = model(X)
    return output

def printname(mon):
    print('{} detected.'.format(mon))
    return True

def runbot():
    printed = False
    while True:
        screenshot = wincap.get_screenshot()[50:,:]
        portshot = portcap.get_screenshot()
        
        # Only performs predictions when a known enemy pokemon portrait is detected
        mon = cl.portraitcheck(portshot)
        if mon:
            if not printed:
                printed = printname(mon)
            array = modelpredict(models[mon], screenshot)
            cl.keypress(array, mon)

        # Mash 'j' if no enemy detected
        else:
            pk.press('j', sec=0.5)
            printed = False

        time.sleep(0.15)

        if kb.is_pressed('q'):
            cl.keyrelease()
            print('Bot has been stopped. Press e again to start bot.')
            return

     
print('Press e to start bot, then press q to quit.')
while True:
    if kb.is_pressed('e'):
        print('Running bot... Press q to quit')
        runbot()
        print('Pres ESC to end script.')
    if kb.is_pressed('esc'):
        break