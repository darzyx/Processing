"""
 * Project [darzyx]
 * Sketch_002: Buckyball
 * by Jose Dario Sanchez
 *
 * A 3D model of Buckminsterfullerene.
 * Created using Python Mode for Processing.
 *
"""

# *************************************************
# Primary
# *************************************************

def setup():
    size(750, 750, P3D)

def draw():
    defaultSettings()
    centerCoordinates()
    spinCam()
    drawBuckyball()

# *************************************************
#  Setup
# *************************************************

def defaultSettings():
    background(0)
    smooth(4)


def centerCoordinates():
    translate(width / 2, height / 2, 0)

def spinCam():
    rotateX(45*sin(((0.075*frameCount) % 360))*DEG_TO_RAD)
    rotateY(45*cos(((0.075*frameCount) % 360))*DEG_TO_RAD)

# *************************************************
# Draw Geometry
# *************************************************

def drawBasics(x, y, z):
    stroke(0, 250, 200)
    noFill()
    pushMatrix()
    translate(x + 100, y, z)
    sphere(10)
    popMatrix()

    stroke(0, 200, 250)
    noFill()
    strokeWeight(4)

    line(x + 100, y, z, x + 50, y, z - 87)
    line(x + 50, y, z - 87, x - 50, y, z - 87)

def drawSmallSection():
    for i in range(0, 5):
        pushMatrix()
        rotateY(i * 72 * DEG_TO_RAD)
        translate(0, 0, 69)
        rotateX(38 * DEG_TO_RAD)
        drawBasics(0, 0, 87)
        popMatrix()

def drawMediumSection():
    for j in range(0, 2):
        pushMatrix()
        rotateY(j * 120 * DEG_TO_RAD)
        translate(0, 0, -87)
        rotateX(-38 * DEG_TO_RAD)
        translate(0, 0, -69)
        drawSmallSection()
        popMatrix()

def drawLargeSection():
    for k in range(1, 4):
        pushMatrix()
        rotateY(k * 120 * DEG_TO_RAD)
        translate(0, 0, -87)
        rotateX(-41.85 * DEG_TO_RAD)
        translate(0, 0, -87)
        drawMediumSection()
        popMatrix()

def drawBuckyball():
    pushMatrix()
    translate(0, 228, 0)
    drawLargeSection()
    popMatrix()

    pushMatrix()
    translate(0, -228, 0)
    rotateX(180 * DEG_TO_RAD)
    drawLargeSection()
    popMatrix()
