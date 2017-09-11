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
    size(500, 500, P3D)

def draw():
    pushMatrix()
    cartesianSystem()
    stars()
    popMatrix()
    
    saveFrame("frames/###.png")

def defaultSettings():
    centerCoordinates()

def centerCoordinates():
    translate(width / 2, height / 2, 0)

def cartesianSystem():
    translate(width / 2, height / 2, 0)
    rotateX(90 * DEG_TO_RAD)

def stars():
    rotateY(0.04 * frameCount)
    background(0)
    
    #dwarf
    for i in range(0, 500):
        stroke(255)
        strokeWeight(0.5)
        point(i * sin(i * i), -150, i * cos(i * i))
    
    #giant
    for i in range(0, 500, 5):
        stroke(230, 200, 200)
        strokeWeight(1)
        point(i * sin(i * i), -150, i * cos(i * i))
        
    #supergiant
    for i in range(0, 500, 10):
        stroke(200, 200, 230)
        strokeWeight(1.5)
        point(i * sin(i * i), -150, i * cos(i * i))