import math
import cmath
from tkinter import *
'''class Mouse(object):
    def init(self, PID, x, y, size = 10):
        self.PID = PID
        self.x = x
        self.y = y
        self.size = size
        self.angle = 0
        data.L = [(data.x,data.y), (data.x,data.y+data.size),
                (data.x+data.size//4,data.y+(data.size*3)//4),
                (data.x+(data.size*19)//40, data.y+(data.size*5)//4),
                (data.x+(data.size*32)//50,data.y+(data.size*47)//40),
                (data.x+(data.size*21)//50,data.y+(data.size*27)//40),
                (data.x+(data.size*48)//60,data.y+(data.size*27)//40)]'''

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

def init(data):
    data.angle = 0
    data.x = data.width//2
    data.y = data.height//2
    data.size = 100
    data.L = [[data.x,data.y], [data.x,data.y+data.size],
                [data.x+data.size//4,data.y+(data.size*3)//4],
                [data.x+(data.size*19)//40, data.y+(data.size*5)//4],
                [data.x+(data.size*32)//50,data.y+(data.size*47)//40],
                [data.x+(data.size*21)//50,data.y+(data.size*27)//40],
                [data.x+(data.size*48)//60,data.y+(data.size*27)//40]]

def mousePressed(event, data):
    # use event.x and event.y
    pass

# This is the rotate mouse function
def keyPressed(event, data):
    if event.keysym == "Left":
        data.angle = cmath.exp((math.pi/4)*1j)
        center = complex(data.L[0][0],data.L[0][1])
        for i in range(1,len(data.L)):
            v = data.angle * (complex(data.L[i][0], data.L[i][1]) - center) + center
            data.L[i][0] = v.real
            data.L[i][1] = v.imag
    elif event.keysym == "Right":
        data.angle = cmath.exp((math.pi/4)*-1j)
        center = complex(data.L[0][0],data.L[0][1])
        for i in range(1,len(data.L)):
            v = data.angle * (complex(data.L[i][0], data.L[i][1]) - center) + center
            data.L[i][0] = v.real
            data.L[i][1] = v.imag
'''            data.L[i][0] -= data.L[0][0]
            data.L[i][1] -= data.L[0][1]
            data.L[i][0] = data.L[i][0]*math.cos(data.angle)+data.L[i][1]*math.sin(data.angle)
            data.L[i][1] = data.L[i][1]*math.sin(data.angle)-data.L[i][1]*math.cos(data.angle)
            data.L[i][0] += data.L[0][0]
            data.L[i][1] += data.L[0][1]
#           data.L[i][0] = data.L[0][0] + d*math.cos(data.angle)
#           data.L[i][1] = data.L[0][1] + d*math.sin(data.angle)
    elif event.keysym == "Right":
        data.angle = math.pi/2
        print(data.L)
        for i in range(1,len(data.L)):
            data.L[i][0] -= data.L[0][0]
            data.L[i][1] -= data.L[0][1]
            data.L[i][0] = data.L[i][0]*math.cos(data.angle)-data.L[i][1]*math.sin(data.angle)
            data.L[i][1] = data.L[i][1]*math.sin(data.angle)+data.L[i][1]*math.cos(data.angle)
            data.L[i][0] += data.L[0][0]
            data.L[i][1] += data.L[0][1]
        print(data.L)
#            data.L[i][0] = data.L[0][0] + d*math.cos(data.angle)
#            data.L[i][1] = data.L[0][1] + d*math.sin(data.angle)'''

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_polygon(data.L)
    canvas.create_polygon([[250, 250], [200.0, 300.0], [213.0, 287.0], [188.0, 312.0], [192.0, 308.0], [217.0, 283.0], [217.0, 283.0]])


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)