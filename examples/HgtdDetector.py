from core.Range1D import Range1D
from core.Point import Point
from core.Grid import Grid
from core.DetectorElement import DetectorElement
from core.Detector import Detector

from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex

def HgtdDetector(rangeR: Range1D,
                 rangeZ: Range1D,
                 rangeInclusive: Range1D) -> Detector:
    detector_center = Point(0.5*(rangeZ.minimum() + rangeZ.maximum()),
                            0.5*(rangeR.minimum() + rangeR.maximum()))
    detector_width = rangeZ.maximum() - rangeZ.minimum()
    detector_height = rangeR.maximum() - rangeR.minimum()
    InclusiveBoundaries = DetectorElement(detector_center, height=detector_height, width=detector_width)
    InclusiveBoundaries.graph.GetXaxis().SetRangeUser(rangeInclusive.minimum(),
                                                      rangeInclusive.maximum())
    InclusiveBoundaries.graph.GetYaxis().SetRangeUser(rangeR.minimum(),
                                                      rangeR.maximum())
    hgtdDetector = Detector(boundaries=InclusiveBoundaries)

    layers = []
    layers.append(DetectorElement(Point(3460, 400), height=560, width=40, angle=0.))
    layers.append(DetectorElement(Point(-3460, 400), height=560, width=40, angle=0.))

    for layer in layers:
        layer.graph.SetFillColorAlpha(38, 0.8)
        hgtdDetector.addElement(layer)
    
    return hgtdDetector
