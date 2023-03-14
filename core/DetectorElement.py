from core.Point import Point
from ROOT import TCanvas, TGraph

class DetectorElement:
    def __init__(self,
                 lowLeft: Point,
                 lowRight: Point,
                 upRight: Point,
                 upLeft: Point):
        self.lowLeft = lowLeft
        self.lowRight = lowRight
        self.upLeft = upLeft
        self.upRight = upRight

        self.graph = TGraph()
        self.graph.SetPoint(0, self.lowLeft.x, self.lowLeft.y)
        self.graph.SetPoint(1, self.lowRight.x, self.lowRight.y)
        self.graph.SetPoint(2, self.upRight.x, self.upRight.y)
        self.graph.SetPoint(3, self.upLeft.x, self.upLeft.y)
        self.graph.SetPoint(4, self.lowLeft.x, self.lowLeft.y)

        self.graph.GetXaxis().SetRangeUser(self.lowLeft.x, self.lowRight.x)
        self.graph.GetYaxis().SetRangeUser(self.lowLeft.y, self.upLeft.y)
        
    def draw(self,
             canvas: TCanvas,
             option: str = "APL") -> None:
        canvas.cd()
        self.graph.Draw(option)
