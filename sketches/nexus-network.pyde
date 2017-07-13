"""
 * Project [darzyx]
 * Sketch_003: Nexus Network
 * by Jose Dario Sanchez
 *
 * A color-gradient network of dots and lines.
 * Created using Python Mode for Processing.
 *
"""
# Global values:
xCoord = []
yCoord = []
nexusCount = 15
xDelta = [0] * nexusCount
yDelta = [0] * nexusCount
counter = [0] * nexusCount
deltaVal = (-2, -1, 0, 1, 2)
interVal = (100, 50, 25)

def setup():
    size(500, 500, P3D)
    frameRate(30)
    assignOrigins()
    smooth()

def draw():
    background(0)
    nexusCluster()

def assignOrigins():
    for i in range(0, nexusCount):
        xCoord.append(int(random(0.20 * width, 0.80 * width)))
        yCoord.append(int(random(0.20 * width, 0.80 * width)))

# Draws each of the moving dots:
def nexusCluster():
    global xDelta, yDelta, counter, deltaVal, interVal
    for i in range(0, nexusCount):
        pushMatrix()
        if (counter[i] <= 0):
            xDelta[i] = deltaVal[int(random(len(deltaVal)))]
            yDelta[i] = deltaVal[int(random(len(deltaVal)))]
            counter[i] = interVal[int(random(len(interVal)))]
        else:
            xCoord[i] += xDelta[i]
            yCoord[i] += yDelta[i]
            counter[i] -= 1
        if (xCoord[i] == width):
            xCoord[i] = 0
        elif (yCoord[i] == height):
            yCoord[i] = 0
        elif (xCoord[i] == 0):
            xCoord[i] = width
        elif (yCoord[i] == 0):
            yCoord[i] = height
        network()
        translate(xCoord[i], yCoord[i], 0)
        stroke(0, 0.34 * xCoord[i], 0.34 * yCoord[i])
        sphere(5)
        popMatrix()

# Draws the lines connecting the dots:
def network():
    for i in range(0, nexusCount):
        for j in range(0, nexusCount):
            if (abs(xCoord[i] - xCoord[j]) < 125 and +
                    abs(yCoord[i] - yCoord[j]) < 125):
                stroke(0.34 * xCoord[i], 0, 0.34 * yCoord[i])
                strokeWeight(0.5)
                line(xCoord[i], yCoord[i], 0, xCoord[j], yCoord[j], 0)
