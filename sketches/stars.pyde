"""
 * Project [darzyx]
 * Sketch_004: Stars
 * by Darzyx
 *
 * Rotating in deep space.
 * Created using Python Mode for Processing.
 *
"""

def setup():
    size(700, 700, P3D)

def draw():
    pushMatrix()
    cartesianSystem()
    stars()
    popMatrix()
    pushMatrix()
    defaultSettings()
    stroke(100, 220, 220)
    strokeWeight(5)
    rectMode(CENTER)
    rect(0, 0, 666, 666)
    popMatrix()

def defaultSettings():
    centerCoordinates()
    smooth(8)
    noFill()

def centerCoordinates():
    translate(width / 2, height / 2, 0)

def cartesianSystem():
    translate(width / 2, height / 2, 0)
    rotateX(90 * DEG_TO_RAD)

def stars():
    rotateY(0.01 * frameCount)
    background(0)
    for i in range(0, 575):
        stroke(255)
        strokeWeight(1)
        point(i * sin(i * i), -150, i * cos(i * i))

    for i in range(0, 575, 5):
        stroke(230, 230, 255)
        strokeWeight(2)
        point(i * sin(i * i), -150, i * cos(i * i))
