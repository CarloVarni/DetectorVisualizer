from core.Point import Point
from ROOT import TCanvas, TGraph
import numpy as np
import math

class DetectorElement:
    # Defined by element Center (Point), height (float), width (float) and rotation (float)
    # Point coordinate: [z, r]
    def __init__(self,
                 center: Point,
                 height: float,
                 width: float,
                 angle: float = 0.):
        self.center = np.array([center.x, center.y])
        self.height = height
        self.width = width
        self.angle = angle

        # Get the corners, traslated to the origin
        lowLeft = np.array([-self.width/2., -self.height/2.])
        lowRight = np.array([self.width/2., -self.height/2.])
        upLeft = np.array([-self.width/2., self.height/2.])
        upRight = np.array([self.width/2., self.height/2.])

        # Rotate
        if self.angle != 0.:
            rotation_angle = self.angle * math.pi / 180.
            rotationMatrix = np.matrix([[math.cos(rotation_angle), -math.sin(rotation_angle)], [math.sin(rotation_angle), math.cos(rotation_angle)]])
            lowLeft = np.dot(rotationMatrix, lowLeft)
            lowRight = np.dot(rotationMatrix, lowRight)
            upLeft = np.dot(rotationMatrix, upLeft)
            upRight = np.dot(rotationMatrix, upRight)
            
            # convert to Array again
            lowLeft = np.squeeze(np.asarray(lowLeft))
            lowRight = np.squeeze(np.asarray(lowRight))
            upLeft = np.squeeze(np.asarray(upLeft))
            upRight = np.squeeze(np.asarray(upRight))
            
        # traslate to center
        lowLeft = lowLeft + self.center
        lowRight = lowRight + self.center
        upLeft = upLeft + self.center
        upRight = upRight + self.center
        
        self.graph = TGraph()
        self.graph.SetPoint(0, lowLeft[0], lowLeft[1])
        self.graph.SetPoint(1, lowRight[0], lowRight[1])
        self.graph.SetPoint(2, upRight[0], upRight[1])
        self.graph.SetPoint(3, upLeft[0], upLeft[1])
        self.graph.SetPoint(4, lowLeft[0], lowLeft[1])

        # This has to be changed!
        self.graph.GetXaxis().SetRangeUser(lowLeft[0], lowRight[0])
        self.graph.GetYaxis().SetRangeUser(lowLeft[1], upLeft[1])
        
    def draw(self,
             canvas: TCanvas,
             option: str = "APL") -> None:
        canvas.cd()
        self.graph.Draw(option)
