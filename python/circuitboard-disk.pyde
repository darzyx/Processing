"""
 * Project [darzyx]
 * Sketch_001: "Circuitboard Disk"
 * by Jose Dario Sanchez
 *
 * A cyberpunk-inspired circuit board disk.
 * Created using Python Mode for Processing.
 *
"""

import math

# ************************************
# Global Variables:
# ************************************

axPxl = 329
ayPxl = 315

bxPxl = 420
byPxl = 315

cxPxl = 330
cyPxl = 435

dxPxl = 330
dyPxl = 435

exPxl = 435
eyPxl = 357

fxPxl = 435
fyPxl = 357

gxPxl = 435
gyPxl = 419

hxPxl = 315
hyPxl = 341

ixPxl = 420
iyPxl = 435

# ************************************
# Primary Functions:
# ************************************

def setup():
    size(750, 750)
    smooth()
    frameRate(100)

def draw():
    background(0)
    noFill()

    drawSqrUnits()
    drawBrake()
    drawTridents()
    drawBorders()
    drawRoundPanels()
    drawWires()
    drawWireAnimation()

# ************************************
# Supplementary Drawing Functions:
# ************************************

def drawSqrUnits():
    rectMode(CENTER)
    stroke(0, 255, 204)
    strokeWeight(0.75)
    noFill()

    for i in range(0, 100, 10):
        rect((width / 2) - 45 + i, (height / 2) - 55, 7, 7)
        rect((width / 2) - 45 + i, (height / 2) + 56, 7, 7)
        rect((width / 2) - 55, (height / 2) - 45 + i, 7, 7)
        rect((width / 2) + 56, (height / 2) - 45 + i, 7, 7)

    stroke(0, 204, 255)
    strokeWeight(3)
    fill(28, 48, 54)

    rect(width / 2, width / 2, 110, 110)
    rect(500, 475, 10, 50)
    rect(515, 475, 10, 50)
    rect(530, 475, 10, 50)
    rect(545, 475, 10, 50)
    rect(200, 275, 10, 50)
    rect(215, 275, 10, 50)
    rect(230, 275, 10, 50)
    rect(245, 275, 10, 50)

def drawBrake():
    stroke(0, 204, 255)
    strokeWeight(7)
    noFill()

    line(width / 2, 675, width / 2, 725)
    line(675, height / 2, 725, height / 2)
    arc(width / 2, height / 2, 700, 700, 0, PI / 2)

    for i in range(3, 89, 2):
        stroke(0, 204, 255)
        strokeWeight(1)

        line((width / 2) + 320 * cos(i * DEG_TO_RAD), (height / 2)
             + 320 * sin(i * DEG_TO_RAD),
             (width / 2) + 335 * cos(i * DEG_TO_RAD), (height / 2)
             + 335 * sin(i * DEG_TO_RAD))

        stroke(0, 255, 204)
        strokeWeight(5)

        point((width / 2) + 335 * cos(i * DEG_TO_RAD),
              (height / 2) + 335 * sin(i * DEG_TO_RAD))

def drawTridents():
    stroke(0, 255, 204)
    strokeWeight(5)

    for i in range(4, 12):
        arc(width / 2, height / 2, 650, 650, (PI / 4.5) + 2 * i *
            (PI / 20), (PI / 4.5) + (PI / 30) + 2 * i * (PI / 20))
        arc(width / 2, height / 2, 630, 630, (PI / 4.5) + 2 * i *
            (PI / 20), (PI / 4.5) + (PI / 20) + 2 * i * (PI / 20))
        arc(width / 2, height / 2, 610, 610, (PI / 4.5) + 2 * i *
            (PI / 20), (PI / 4.5) + (PI / 30) + 2 * i * (PI / 20))

def drawBorders():
    stroke(0, 255, 204)
    strokeWeight(3)

    for i in range(110, 175, 5):
        point((width / 2) + 355 * cos(i * DEG_TO_RAD), (height / 2)
              + 355 * sin(i * DEG_TO_RAD))

    stroke(0, 204, 255)
    strokeWeight(5)

    arc(width / 2, height / 2, 525, 525, PI / 3.5, 2.15 * PI)

    strokeWeight(3)

    arc(width / 2, height / 2, 685, 685, 0.55 * PI, 1.67 * PI)

    strokeWeight(2)

    arc(width / 2, height / 2, 725, 725, PI, 1.67 * PI)

    strokeWeight(1.5)

    arc(width / 2, height / 2, 510, 510, PI / 3.5, 2.15 * PI)

def drawRoundPanels():
    stroke(0, 255, 204)
    strokeWeight(2)
    fill(28, 48, 54)

    for i in range(315, 360, 15):
        ellipse((width / 2) + 330 * cos(i * DEG_TO_RAD),
                (height / 2) + 330 * sin(i * DEG_TO_RAD), 80, 80)

def drawWires():
    # TOP
    if (millis() % 2 == 0):
        stroke(50, 255, 50)
    elif (millis() % 5 == 0):
        stroke(50, 50, 255)
    else:
        stroke(255, 50, 50)
    strokeWeight(0.5)

    line(329, 315, 329, 140)
    line(329, 180, 306, 156)
    line(306, 156, 306, 130)
    line(329, 190, 296, 156)
    line(296, 156, 296, 133)
    line(329, 200, 286, 156)
    line(286, 156, 286, 136)
    line(338, 315, 338, 250)
    line(400, 315, 400, 275)
    line(409, 315, 409, 275)
    line(409, 275, 479, 205)
    line(479, 205, 479, 143)
    line(439, 245, 439, 200)
    line(449, 235, 449, 200)
    line(420, 315, 420, 275)
    line(420, 275, 440, 255)
    line(440, 255, 500, 255)
    line(500, 255, 525, 230)
    line(525, 230, 584, 230)
    line(560, 230, 560, 201)
    line(550, 230, 550, 220)
    line(550, 220, 490, 220)
    line(490, 220, 490, 210)
    line(490, 210, 550, 210)
    line(550, 210, 550, 200)
    line(550, 200, 490, 200)
    line(490, 200, 490, 190)
    line(490, 190, 520, 190)
    line(379, 315, 379, 200)
    line(379, 200, 439, 140)
    line(439, 140, 439, 128)

    stroke(255, 20, 147)
    fill(255, 20, 147)

    ellipse(329.5, 140, 5, 5)
    ellipse(338, 250, 5, 5)
    ellipse(400, 275, 5, 5)
    ellipse(439, 200, 5, 5)
    ellipse(449, 200, 5, 5)
    ellipse(520, 190, 5, 5)

    # RIGHT
    if (millis() % 2 == 0):
        stroke(50, 50, 255)
    elif (millis() % 3 == 0):
        stroke(50, 255, 50)
    else:
        stroke(255, 50, 50)
    strokeWeight(0.5)

    line(435, 330, 460, 330)
    line(435, 339, 475, 339)
    line(435, 348, 490, 348)
    line(435, 357, 505, 357)
    line(505, 357, 525, 377)
    line(525, 377, 630, 377)
    line(550, 377, 550, 320)
    line(550, 320, 530, 300)
    line(550, 320, 570, 300)
    line(435, 389, 600, 389)
    line(435, 419, 460, 419)
    line(460, 419, 480, 439)
    line(480, 439, 560, 439)
    line(560, 439, 590, 469)
    line(480, 439, 480, 520)
    line(480, 520, 510, 550)

    stroke(255, 20, 147)
    fill(255, 20, 147)

    ellipse(460, 330, 5, 5)
    ellipse(475, 339, 5, 5)
    ellipse(490, 348, 5, 5)
    ellipse(600, 389, 5, 5)
    ellipse(590, 469, 5, 5)
    ellipse(510, 550, 5, 5)
    ellipse(530, 300, 5, 5)
    ellipse(570, 300, 5, 5)

    # BOTTOM
    if (millis() % 2 == 0):
        stroke(255, 50, 50)
    elif (millis() % 5 == 0):
        stroke(50, 255, 50)
    else:
        stroke(50, 50, 255)
    strokeWeight(0.5)

    line(420, 435, 420, 550)
    line(420, 475, 435, 500)
    line(420, 475, 405, 500)
    line(405, 500, 405, 525)
    line(435, 500, 435, 525)
    line(420, 550, 477, 607)
    line(350, 435, 350, 500)
    line(330, 435, 330, 475)
    line(330, 475, 300, 475)
    line(300, 475, 300, 500)
    line(300, 500, 200, 500)
    line(200, 500, 200, 525)
    line(220, 500, 220, 540)
    line(240, 500, 240, 555)
    line(260, 500, 260, 570)
    line(350, 500, 375, 525)
    line(375, 525, 375, 575)
    line(375, 575, 350, 600)
    line(350, 600, 350, 628)
    line(339, 435, 339, 515)
    line(339, 515, 269, 585)
    line(309, 545, 309, 620)
    line(269, 585, 269, 607)

    stroke(255, 20, 147)
    fill(255, 20, 147)

    ellipse(405, 525, 5, 5)
    ellipse(435, 525, 5, 5)
    ellipse(200, 525, 5, 5)
    ellipse(220, 540, 5, 5)
    ellipse(240, 555, 5, 5)
    ellipse(260, 570, 5, 5)

    # LEFT
    if (millis() % 2 == 0):
        stroke(50, 255, 50)
    elif (millis() % 5 == 0):
        stroke(255, 50, 50)
    else:
        stroke(50, 50, 255)
    strokeWeight(0.5)

    line(315, 401, 275, 401)
    line(315, 410, 205, 410)
    line(315, 419, 275, 419)
    line(275, 419, 255, 439)
    line(275, 401, 255, 381)
    line(225, 410, 175, 360)
    line(225, 410, 175, 460)
    line(175, 360, 120, 360)
    line(315, 329, 300, 329)
    line(300, 329, 280, 309)
    line(280, 309, 185, 309)
    line(280, 309, 280, 280)
    line(185, 309, 155, 279)
    line(280, 280, 320, 240)
    line(320, 240, 320, 210)
    line(320, 210, 270, 160)
    line(315, 350, 200, 350)
    line(200, 350, 155, 305)
    line(315, 341, 250, 341)
    line(250, 341, 250, 310)

    stroke(255, 20, 147)
    fill(255, 20, 147)

    ellipse(255, 439, 5, 5)
    ellipse(255, 381, 5, 5)
    ellipse(205, 410, 5, 5)
    ellipse(175, 460, 5, 5)
    ellipse(155, 279, 5, 5)
    ellipse(270, 160, 5, 5)
    ellipse(155, 305, 5, 5)

# ************************************
# Supplementary Animation Functions
# ************************************

def drawWireAnimation():
    # Each animation is enclosed by a (push/pop)Matrix().
    if (millis() % 2 == 0):
        stroke(0, 255, 204)
    elif (millis() % 3 == 0):
        stroke(0, 204, 255)
    else:
        stroke(255, 20, 147)
    strokeWeight(3)

    pushMatrix()
    global axPxl
    global ayPxl
    point(axPxl, ayPxl)
    if axPxl == 329 and ayPxl > 190:
        ayPxl -= 5
    elif axPxl > 296 and ayPxl > 156:
        axPxl -= 1
        ayPxl -= 1
    elif axPxl == 296 and ayPxl > 134:
        ayPxl -= 1
    else:
        axPxl = 329
        ayPxl = 315
    popMatrix()

    pushMatrix()
    global bxPxl
    global byPxl
    point(bxPxl, byPxl)
    if bxPxl == 420 and byPxl > 275:
        byPxl -= 5
    elif bxPxl <= 440 and byPxl >= 256:
        bxPxl += 2
        byPxl -= 2
    elif bxPxl <= 500 and byPxl >= 230:
        bxPxl += 1
    elif bxPxl <= 525 and byPxl >= 230:
        bxPxl += 1
        byPxl -= 1
    elif bxPxl <= 550 and byPxl >= 230:
        bxPxl += 2
    elif bxPxl >= 550 and byPxl > 220:
        byPxl -= 5
    elif bxPxl > 490 and byPxl == 220:
        bxPxl -= 2
    elif bxPxl == 490 and byPxl > 210:
        byPxl -= 5
    elif bxPxl < 550 and byPxl == 210:
        bxPxl += 2
    elif bxPxl == 550 and byPxl > 200:
        byPxl -= 5
    elif bxPxl > 490 and byPxl == 200:
        bxPxl -= 2
    elif bxPxl == 490 and byPxl > 190:
        byPxl -= 5
    elif bxPxl < 518 and byPxl == 190:
        bxPxl += 2
    else:
        bxPxl = 420
        byPxl = 315
    popMatrix()

    pushMatrix()
    global cxPxl
    global cyPxl
    point(cxPxl, cyPxl)
    if cxPxl == 330 and cyPxl < 475:
        cyPxl += 5
    elif cxPxl > 300 and cyPxl == 475:
        cxPxl -= 1
    elif cxPxl == 300 and cyPxl < 500:
        cyPxl += 1
    elif cxPxl > 240 and cyPxl == 500:
        cxPxl -= 2
    elif cxPxl == 240 and cyPxl < 550:
        cyPxl += 2
    else:
        cxPxl = 330
        cyPxl = 435
    popMatrix()

    pushMatrix()
    global dxPxl
    global dyPxl
    point(dxPxl, dyPxl)
    if dxPxl == 330 and dyPxl < 475:
        dyPxl += 5
    elif dxPxl > 300 and dyPxl == 475:
        dxPxl -= 5
    elif dxPxl == 300 and dyPxl < 500:
        dyPxl += 1
    elif dxPxl > 200 and dyPxl == 500:
        dxPxl -= 2
    elif dxPxl == 200 and dyPxl < 517:
        dyPxl += 2
    else:
        dxPxl = 330
        dyPxl = 435
    popMatrix()

    pushMatrix()
    global exPxl
    global eyPxl
    point(exPxl, eyPxl)
    if exPxl < 505 and eyPxl == 357:
        exPxl += 5
    elif exPxl < 525 and eyPxl < 377:
        exPxl += 1
        eyPxl += 1
    elif exPxl < 550 and eyPxl == 377:
        exPxl += 1
    elif exPxl == 550 and eyPxl > 320:
        eyPxl -= 1
    elif exPxl < 568 and eyPxl > 302:
        exPxl += 1
        eyPxl -= 1
    else:
        exPxl = 435
        eyPxl = 357

    popMatrix()

    pushMatrix()
    global fxPxl
    global fyPxl
    point(fxPxl, fyPxl)
    if fxPxl < 505 and fyPxl == 357:
        fxPxl += 5
    elif fxPxl < 525 and fyPxl < 377:
        fxPxl += 1
        fyPxl += 1
    elif fxPxl < 550 and fyPxl == 377:
        fxPxl += 1
    elif fxPxl == 550 and fyPxl > 320:
        fyPxl -= 1
    elif fxPxl > 532 and fyPxl > 302:
        fxPxl -= 1
        fyPxl -= 1
    else:
        fxPxl = 435
        fyPxl = 357
    popMatrix()

    pushMatrix()
    global gxPxl
    global gyPxl
    point(gxPxl, gyPxl)

    if gxPxl < 460 and gyPxl == 419:
        gxPxl += 5
    elif gxPxl < 480 and gyPxl < 439:
        gxPxl += 1
        gyPxl += 1
    elif gxPxl < 560 and gyPxl == 439:
        gxPxl += 2
    elif gxPxl < 586 and gyPxl < 466:
        gxPxl += 1
        gyPxl += 1
    else:
        gxPxl = 435
        gyPxl = 419
    popMatrix()

    pushMatrix()
    global hxPxl
    global hyPxl
    point(hxPxl, hyPxl)
    if hxPxl > 250 and hyPxl == 341:
        hxPxl -= 5
    elif hxPxl == 250 and hyPxl > 310:
        hyPxl -= 1
    elif hxPxl > 185 and hyPxl == 310:
        hxPxl -= 1
    elif hxPxl > 157 and hyPxl > 282:
        hxPxl -= 1
        hyPxl -= 1
    else:
        hxPxl = 315
        hyPxl = 341
    popMatrix()

    pushMatrix()
    global ixPxl
    global iyPxl
    point(ixPxl, iyPxl)
    if ixPxl == 420 and iyPxl < 550:
        iyPxl += 1
    elif ixPxl < 475 and iyPxl < 605:
        ixPxl += 5
        iyPxl += 5
    else:
        ixPxl = 420
        iyPxl = 435

    popMatrix()
