'''
Functions, lists, tuples and dictionaries shared between multiple notebooks and scripts were put in this module.
'''

import pyKey as pk
from vision import Vision
import keyboard as kb

# Defining list of all potential opponent pokemon
opponents = ['poliwrath', 'heracross', 'mienshao']

# Defining dictionary of vision objects for all opponents
portraits = {mon: Vision('../data/portrait/{}.png'.format(mon)) for mon in opponents}

# Defining list for all keyboard controls, directional controls, and attack controls
controls  = ['SPACEBAR', 'a', 's', 'd', 'j', 'k', 'l']
d_controls = controls[:4]
a_controls = controls[4:]

# Function to check if there is a known enemy portrait on screen
def portraitcheck(port_img):
    for mon, vis in portraits.items():
        if vis.find(port_img, threshold=0.75):
            return mon
    return False

# Function to translate input array into keys
def translate(arr):
    result = []
    for x, y in zip(controls, arr):
        if (x * y):
            result.append(x * y)
    return result

# Keylogging function
def keylog():
    output = []
    for key in controls:
        if kb.is_pressed(key):
            output.append(1)
        else:
            output.append(0)
    return output

# Function for releasing all keys
def keyrelease():
    for key in controls:
        pk.releaseKey(key)

'''
Function for performing keyboard input based on input array
'''
# Dictionary of thresholds for each model, to be used in keypress function
tdict = {'poliwrath':
            {'spacet': 0.09,
             'st': 0.25,
             'atkt': 0.4},
        'heracross':
            {'spacet': 0.28,
             'st': 0.2,
             'atkt': 0.4},
        'mienshao':
            {'spacet': 0.12,
             'st': 0.25,
             'atkt': 0.43}}

def keypress(arr, mon):
    keyrelease()

    # 1) Check if going left or right ['a' or 'd']
    if abs(arr[0][1] - arr[0][3]) > 0.05:
        pk.pressKey('a') if (arr[0][1] > arr[0][3]) else pk.pressKey('d')

    # 2) Check if jumping or crouching ['SPACEBAR' or 's']
    if arr[0][0] > tdict[mon]['spacet']:
        pk.pressKey('SPACEBAR')
    if arr[0][2] > tdict[mon]['st']:
        pk.pressKey('s')
    
    # 3) Check if attacking
    if arr[0][7] > tdict[mon]['atkt']:
        # If attacking, get index of max attack, then perform attack
        listarr = arr.tolist()[0][4:7]
        max_ind = listarr.index(max(listarr))
        pk.pressKey(a_controls[max_ind])

