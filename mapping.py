#import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event2')

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291
lBtn = 292
rBtn = 293
selBtn = 296
staBtn = 297

#display codes
for event in gamepad.read_loop():
    #buttons 
    if event.type == ecodes.EV_KEY:
        print(event)
        if event.value == 1:
            if event.code == xBtn:
                print("X")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
                print("A")
            elif event.code == yBtn:
                print("Y")
            elif event.code == lBtn:
                print("LEFT")
            elif event.code == rBtn:
                print("RIGHT")
            elif event.code == selBtn:
                print("Select")
            elif event.code == staBtn:
                print("Start")
        elif event.value == 0:
          print("Release")

    #Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             if absevent.event.value == 0:
                print("Left")
             elif absevent.event.value == 255:
                print("Right")
             elif absevent.event.value == 127:
                print("Center")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             if absevent.event.value == 0:
                print("Up")
             elif absevent.event.value == 255:
                print("Down")
             elif absevent.event.value == 127:
                print("Center")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_BRAKE":
            print("Left Trigger")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_GAS":
            print("Right Trigger")
