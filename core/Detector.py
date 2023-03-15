from core.DetectorElement import DetectorElement
from ROOT import TCanvas

class Detector:
    def __init__(self,
                 boundaries: DetectorElement):
        self.boundaries = boundaries
        self.elements = []

    def addElement(self,
                   element: DetectorElement) -> None:
        self.elements.append(element)

    def draw(self, canvas: TCanvas) -> None:
        # Draw the detector canvas
        self.boundaries.graph.GetXaxis().SetTitle("z [mm]")
        self.boundaries.graph.GetYaxis().SetTitle("radius [mm]")
        self.boundaries.graph.SetLineColor(0)
        self.boundaries.graph.SetMarkerColor(0)
        self.boundaries.graph.SetFillColor(0)
        self.boundaries.graph.SetMarkerSize(0)
        self.boundaries.draw(canvas, "AP")

        # Draw the other elements
        for element in self.elements:
            element.draw(canvas, "FLSAME")

