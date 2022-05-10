import numpy as np
# from scipy.spatial.transform import Rotation


class Frame:
    name = None
    frames = []
    parentFrame = None
    points = None
    originalPoints = None
    localOrigin = np.array([[0], [0], [0]])  # need to figure out what this is used for
    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # not used

    def __init__(self, name, p):
        if self.isSubFrame():
            self.points = self.shift(super.getOrigin())
        else:
            self.points = p
            self.originalPoints = p
        self.name = name
    
    def setParent(self, parent):
        self.parentFrame = parent
        self.setOrigin(np.add(parent.getOrigin(), self.localOrigin))
        self.points = self.originalPoints
        self.shift(self.getOrigin())

    def addFrame(self, frame):
        self.frames.append(frame)
        print(self.name)
        print(self.frames)

    def setOrigin(self, o):
        self.localOrigin = o
    
    def getOrigin(self):
        return self.localOrigin

    def print(self):
        print(np.array2string(self.getPoints()))

    def getPoints(self):
        returned = [self.getOwnPoints()]
        for f in self.frames:
            if len(f.getOwnPoints()) == 3 and len(f.getOwnPoints()[0]) == 1:
                returned.append(f.getOwnPoints())
            else:
                for p in f.getOwnPoints():
                    returned.append(p)
        return returned

    def getOwnPoints(self):
        return self.points

    def getChildPoints(self):
        returned = []
        for f in self.frames:
            named = [f.getName()]
            returned.append(named.append(f.getPoints()))

    def shift(self, vector):
        returned = np.array([[[0], [0], [0]]])
        for p in self.points:
            returned = np.concatenate((returned, [np.add(p, vector)]), axis=0)
        self.points = returned[1:]
        # for f in self.frames:
        #     f.shift(vector)

    def rotateWithMatrix(self, matrix):
        self.points = np.matmul(matrix, self.points)
        for f in self.frames:
            f.rotateWithMatrix(matrix)

    def rotateAboutAxis(self, vector, angle):
        a = angle
        unitVector = vector/np.linalg.norm(vector)
        ux = unitVector[0]
        uy = unitVector[1]
        uz = unitVector[2]
        matrix = np.array([[np.cos(a) + ux ** 2 * (1-np.cos(a)), ux * uy * (1 - np.cos(a)) - uz * np.sin(a), ux * uz * (1 - np.cos(a) + uy * np.sin(a))],
                           [uy * ux * (1 - np.cos(a)) + uz * np.sin(a), np.cos(a) + uy ** 2 * (1 - np.cos(a)), uy * uz * (1 - np.cos(a)) - ux * np.sin(a)],
                           [uz * ux * (1 - np.cos(a) - uy * np.sin(a)), uz * uy * (1 - np.cos(a) + ux * np.sin(a)), np.cos(a) + uz ** 2 * (1 - np.cos(a))]])
        self.rotateWithMatrix(matrix)
        return self.points

    def rotateAboutLine(self, origin, vector, angle):
        self.shift(np.matmul(-1, origin))
        self.rotateAboutAxis(vector, angle)
        self.shift(origin)

    def isSubFrame(self):
        return self.parentFrame != None


class rotateJoint(Frame):
    axis = None

    def __init__(self, name, axis, p):
        self.axis = axis
        super().__init__(name, p)

    def rotateCW(self, a):
        super().rotateAboutAxis(self.axis, a)

    def rotateCCW(self, a):
        super().rotateAboutAxis(self.axis, -1 * a)
    
    def rotateWithMatrix(self, matrix):
        self.points = np.matmul(matrix, self.points)
        for f in self.frames:
            f.rotateWithMatrix(matrix)
        self.axis = np.matmul(matrix, self.axis)
    


class linkage(Frame):
    def __init__(self, name, p):
        super().__init__(name, p)
        if len(super().getOwnPoints()) != 2:
            print("invalid linkage has " + len(super().getOwnPoints()) + " points")
        super().setOrigin(p[1])
        print(p[1])
