


unitSize = float(100)
eqTriH = float(0.8660254)

def setup():
    size(700, 700)

def draw():
    translate(width / 2, height / 2)
    rotate(0.1*sin(0.1*frameCount))
    rotate(frameCount*0.01)
    background(0)
    strokeWeight(2)
    noFill()
    
    angle = 0
    radial = 0
    for i in range(0, 25):
        pushMatrix()
        r = 150
        g = 50
        b = 200 + 50*sin(frameCount)
        stroke(r, g, b)
        translate(radial * cos(angle), radial * sin(angle))
        rotate(angle)
        beginShape()
        for k in range(0, 6):
            vertex(unitSize + cos(TWO_PI / 6 * k) * unitSize,
                   unitSize * eqTriH + sin(TWO_PI / 6 * k) * unitSize)
        endShape(CLOSE)
        popMatrix()
        
        angle += 3
        radial += random(7)
        
    