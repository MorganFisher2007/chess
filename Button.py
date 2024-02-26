from graphics import *

# creating Button class
class Button:
    # constructor method
    def __init__(self, center, width, height, label, color):
        # creating instance variables with normal parameters
        self.center = center
        self.width = width
        self.height = height
        self.label = Text(self.center, label)
        self.color = color

        # finding the endpoints of a button rectangle using center and width
        self.p1 = Point(self.center.getX() - width/2, self.center.getY() - height/2)
        self.p2 = Point(self.center.getX() + width/2, self.center.getY() + height/2)

        # creating rectangle instance variable with self.p1 and self.p2
        self.outline = Rectangle(self.p1, self.p2)

        self.img = False
        self.deactivate()

    def draw(self, win):
        "draws button"
        self.outline.draw(win)
        self.label.draw(win)
        if self.img:
            self.img_obj.draw(win)

    def undraw(self):
        "undraws button"
        self.deactivate()
        self.outline.undraw()
        self.label.undraw()
        if self.img:
            self.img_obj.undraw(win)

    def activate(self):
        "makes button clickable"
        self.active = True
        self.label.setFill("black")
        self.label.setStyle("normal")
        self.outline.setFill(self.color)
        self.outline.setWidth(2)

    def deactivate(self):
        "makes button unclickable"
        self.active = False
        self.label.setFill("grey")
        self.label.setStyle("italic")
        self.outline.setFill("grey89")
        self.outline.setWidth(1)

    def setLabel(self, new_label):
        "sets button label"
        self.label.setText(new_label)
    
    def getLabel(self):
        "gets button label"
        return self.label.getText()

    def clicked(self, point):
        "checks if button is clicked and returns a clicked state"
        wasClicked = False

        # checks if pt is within the button's rectangle (self.p1 and self.p2)
        if self.p1.getX() <= point.getX() <= self.p2.getX():
            if self.p1.getY() <= point.getY() <= self.p2.getY():
                if self.active == True:
                    wasClicked = True

        # returning clicked state
        return wasClicked

    def checkActive(self):
        "checks if button is active"
        return self.active

    def setSize(self, point):
        self.label.setSize(point)

    def setFill(self, color):
        self.color = color

    def getFill(self):
        return self.color

    def setIMG(self, img_file):
        self.img = True
        self.img_obj = Image(self.center, img_file)
        
