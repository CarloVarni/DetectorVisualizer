from core.Range1D import Range1D
from core.Point import Point
from core.Grid import Grid
from core.DetectorElement import DetectorElement
from core.Detector import Detector

from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex

def ITkStripDetector(rangeR: Range1D,
                     rangeZ: Range1D,
                     rangeInclusive: Range1D) -> Detector:
    # Inclusive Boundaries for the entire detector
    detector_center = Point(0.5*(rangeZ.minimum() + rangeZ.maximum()),
                            0.5*(rangeR.minimum() + rangeR.maximum()))
    detector_width = rangeZ.maximum() - rangeZ.minimum()
    detector_height = rangeR.maximum() - rangeR.minimum()
    InclusiveBoundaries = DetectorElement(detector_center, height=detector_height, width=detector_width)
    InclusiveBoundaries.graph.GetXaxis().SetRangeUser(rangeInclusive.minimum(),
                                                      rangeInclusive.maximum())
    InclusiveBoundaries.graph.GetYaxis().SetRangeUser(rangeR.minimum(),
                                                      rangeR.maximum())
    stripDetector = Detector(boundaries=InclusiveBoundaries)

    # underflow
    underflow_center = Point(0.5*(rangeZ.minimum() + rangeInclusive.minimum()),
                             0.5*(rangeR.minimum() + rangeR.maximum()))
    underflow_width = rangeZ.minimum() - rangeInclusive.minimum()
    underflowArea = DetectorElement(underflow_center, height=detector_height, width=underflow_width)
    underflowArea.graph.SetFillColorAlpha(18, 0.6)
    stripDetector.addElement(underflowArea)

    # overflow
    overflow_center = Point(0.5*(rangeZ.maximum() + rangeInclusive.maximum()),
                            0.5*(rangeR.minimum() + rangeR.maximum()))
    overflow_width = rangeInclusive.maximum() - rangeZ.maximum()
    overflowArea = DetectorElement(overflow_center, height=detector_height, width=overflow_width)
    overflowArea.graph.SetFillColorAlpha(18, 0.6)
    stripDetector.addElement(overflowArea)

    # Barrel
    barrel_layers = []
    barrel_layers.append(DetectorElement(Point(0, 401.8), height=28.2, width=2721, angle=0.))
    barrel_layers.append(DetectorElement(Point(0, 564), height=26.5, width=2721, angle=0.))
    barrel_layers.append(DetectorElement(Point(0, 763.5), height=26.5, width=2697, angle=0.))
    barrel_layers.append(DetectorElement(Point(0, 1001), height=25, width=2697, angle=0.))

    for layer in barrel_layers:
        layer.graph.SetFillColorAlpha(38, 0.8)
        stripDetector.addElement(layer)

    # Endcap
    endcap_layers = []
    endcap_layers.append(DetectorElement(Point(-1512, 665.85), height=543.72, width=21.5))
    endcap_layers.append(DetectorElement(Point(-1702, 665.85), height=543.72, width=21.5))
    endcap_layers.append(DetectorElement(Point(-1952, 665.85), height=543.72, width=21.5))
    endcap_layers.append(DetectorElement(Point(-2237, 665.85), height=543.72, width=21.5))
    endcap_layers.append(DetectorElement(Point(-2532, 665.85), height=543.72, width=21.5))
    endcap_layers.append(DetectorElement(Point(-2850, 665.85), height=543.72, width=21.5))

    for layer in endcap_layers:
        layer.graph.SetFillColorAlpha(38, 0.8)
        stripDetector.addElement(layer)
        mirrored = DetectorElement(Point(-layer.center[0], layer.center[1]), height=layer.height, width=layer.width)
        mirrored.graph.SetFillColorAlpha(38, 0.8)
        stripDetector.addElement(mirrored)
        
    return stripDetector

