import pyautogui
import ctypes
import time
import win32api
import random
import keyboard



# Parse the data from the text file
dx_values = [
-0.36*0.45,
-0.08*0.45,
0.11 *0.45,
-0.41*0.45,
-0.03*0.45,
-0.57*0.45,
-0.16*0.45,
0.26 *0.45,
-0.44*0.45,
0.02 *0.45,
0.54 *0.45,
0.58 *0.45,
0.41 *0.45,
0.33 *0.45,
-0.17*0.45,
-0.54*0.45,
-0.28*0.45,
-0.05*0.45,
 0.23*0.45 ,
 0.46*0.45 ,
 0.17*0.45 ,
 0.21*0.45 ,
 0.26*0.45 ,
-0.35*0.45,
 0.20*0.45 ,
 0.70*0.45 ,
 0.40*0.45  ]

dy_values = [
-0.49,
-0.58,
-0.66,
-0.45,
-0.72,
-0.39,
-0.62,
-0.59,
-0.49,
-0.35,
-0.13,
0.05 ,
-0.20,
-0.26,
-0.16,
0.02 ,
0.02 ,
-0.19,
-0.10,
0.00 ,
-0.09,
0.05 ,
-0.18,
-0.10,
-0.25,
0.00 ,
0.01]

# "bullet_0"      "-0.36   -0.49   0.00  0.00"
# "bullet_1"      "-0.08   -0.58   0.00  0.00"
# "bullet_2"      " 0.11   -0.66   0.30  0.20"
# "bullet_3"      "-0.41   -0.45   0.40  0.25"
# "bullet_4"      "-0.03   -0.72   0.20  0.15"
# "bullet_5"      "-0.57   -0.39   0.35  0.30"
# "bullet_6"      "-0.16   -0.62   0.25  0.20"
# "bullet_7"      " 0.26   -0.59   0.40  0.30"
# "bullet_8"      "-0.44   -0.49   0.40  0.30"
# "bullet_9"      " 0.02   -0.35   0.25  0.15"
# "bullet_10"     " 0.54   -0.13   0.25  0.15"
# "bullet_11"     " 0.58    0.05   0.25  0.15"
# "bullet_12"     " 0.41   -0.20   0.25  0.15"
# "bullet_13"     " 0.33   -0.26   0.25  0.15"
# "bullet_14"     "-0.17   -0.16   0.25  0.15"
# "bullet_15"     "-0.54    0.02   0.30  0.20"
# "bullet_16"     "-0.28    0.02   0.30  0.20"
# "bullet_17"     "-0.05   -0.19   0.30  0.20"
# "bullet_18"     " 0.23   -0.10   0.30  0.20"
# "bullet_19"     " 0.46    0.00   0.30  0.20"
# "bullet_20"     " 0.17   -0.09   0.30  0.20"
# "bullet_21"     " 0.21    0.05   0.30  0.20"
# "bullet_22"     " 0.26   -0.18   0.30  0.20"
# "bullet_23"     "-0.35   -0.10   0.30  0.20"
# "bullet_24"     " 0.20   -0.25   0.40  0.25"
# "bullet_25"     " 0.70    0.00   0.40  0.25"
# "bullet_26"     " 0.40    0.01   0.40  0.25"

horizontal_range = 2
# min_vertical = 3
# max_vertical = 5
min_firerate = 0.03
max_firerate = 0.04
toggle_button = 'caps lock'
enabled = False

def is_mouse_down():   # verifica daca mouse ul este apasat
    lmb_state = win32api.GetKeyState(0x01)  # ia state-ul key-ului LMB care are valoarea 0x01 in windowsAPI. RMB are 0x02, ENTER are 0x0D etc.
    return lmb_state < 0  # returns 0 daca LMB este apasat. lmb_state < 0 daca este apasat si lmb_state > 0 daca nu este apasat.

print("Anti-recoil script started!")
if enabled:   #enabled are val initiala 0 (False).
    print("ENABLED")
else:
    print("DISABLED")

last_state = False
vertical_o = 0
while True:
    key_down = keyboard.is_pressed(toggle_button)  #are val True daca tasta toggle_button e apasata.
    for i in range(1,13): #de la 1 la 12 cate taste function sunt. adica F1, F2, F3 etc.
        k = keyboard.is_pressed('f'+str(i)) # verifica ce tasta function e apasata
        if k == True:
            vertical_o = i #vertical_o care controleaza reculu ia val lu i care e nr de la tasta function
            break
    #print(vertical_o)
    if key_down != last_state:  #vedem daca s a schimbat starea lu key_down, adica a fost apasata tasta toggle_down
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil ENABLED")
            else:
                print("Anti-recoil DISABLED")
################test
#    if is_mouse_down() and enabled:
#        if is_mouse_down():
#            for i in range(len(dx_values)):
#                    event = ctypes.c_ulong(0x0001)
#                    x = ctypes.c_long(int(dx_values[i]*(16)))
#                    y = ctypes.c_long(int(dy_values[i]*(-16)))
#                    ctypes.windll.user32.mouse_event(event, x, y, 0, 0)
#                    time.sleep(0.05346153846)
############
    if is_mouse_down() and enabled:
        for i in range(len(dx_values)):
            if is_mouse_down():
                event = ctypes.c_ulong(0x0001)
                x = ctypes.c_long(int(dx_values[i]*(13)))
                y = ctypes.c_long(int(dy_values[i]*(-13)))
                ctypes.windll.user32.mouse_event(event, x, y, 0, 0)
            else:
                break
            time.sleep(0.061)
    time.sleep(0.001)


