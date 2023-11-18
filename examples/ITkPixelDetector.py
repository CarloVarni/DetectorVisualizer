from core.Range1D import Range1D
from core.Point import Point
from core.Grid import Grid
from core.DetectorElement import DetectorElement
from core.Detector import Detector

from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex

def ITkPixelDetector(rangeR: Range1D,
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
    pixelDetector = Detector(boundaries=InclusiveBoundaries)

    # underflow
    underflow_center = Point(0.5*(rangeZ.minimum() + rangeInclusive.minimum()),
                             0.5*(rangeR.minimum() + rangeR.maximum()))
    underflow_width = rangeZ.minimum() - rangeInclusive.minimum()
    underflowArea = DetectorElement(underflow_center, height=detector_height, width=underflow_width)
    underflowArea.graph.SetFillColorAlpha(18, 0.6)
    pixelDetector.addElement(underflowArea)

    # overflow
    overflow_center = Point(0.5*(rangeZ.maximum() + rangeInclusive.maximum()),
                            0.5*(rangeR.minimum() + rangeR.maximum()))
    overflow_width = rangeInclusive.maximum() - rangeZ.maximum()
    overflowArea = DetectorElement(overflow_center, height=detector_height, width=overflow_width)
    overflowArea.graph.SetFillColorAlpha(18, 0.6)
    pixelDetector.addElement(overflowArea)

    # Flat Barrel
    flat_barrel_layers = []
    flat_barrel_layers.append(DetectorElement(Point(0, 34.5), height=4.6, width=2*243, angle=0.))
    flat_barrel_layers.append(DetectorElement(Point(0, 99), height=9.4, width=2*245, angle=0.))
    flat_barrel_layers.append(DetectorElement(Point(0, 160), height=11.5, width=374*2, angle=0.))
    flat_barrel_layers.append(DetectorElement(Point(0, 228), height=9.6, width=374*2, angle=0.))
    flat_barrel_layers.append(DetectorElement(Point(0, 291), height=9.5, width=374*2, angle=0.))

    for layer in flat_barrel_layers:
        layer.graph.SetFillColorAlpha(38, 0.8)
        pixelDetector.addElement(layer)

    # Inner Endcap
    inner_endcap_layers = []
    # Inner Rings - Singles
    inner_endcap_layers.append(DetectorElement(Point(263, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(291, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(322, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(357, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(396, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(437, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(486, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(543, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(604, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(675, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(749, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(835, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(925, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1026, 42.8), height=20.1, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1142, 42.8), height=20.1, width=4, angle=0.))
#    inner_endcap_layers.append(DetectorElement(Point(1026, 44.9), height=15.8, width=4, angle=0.))
#    inner_endcap_layers.append(DetectorElement(Point(1142, 47.5), height=11.55, width=4, angle=0.))

    # Intermediate Rings
    inner_endcap_layers.append(DetectorElement(Point(1103, 68.3), height=19.7, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1229, 68.3), height=19.7, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1359, 68.3), height=19.7, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1503, 68.3), height=19.7, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1665, 68.3), height=19.7, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1846, 68.3), height=19.7, width=4, angle=0.))
#    inner_endcap_layers.append(DetectorElement(Point(1665, 69.85), height=18.1, width=4, angle=0.))
#    inner_endcap_layers.append(DetectorElement(Point(1846, 73.14), height=11.4, width=4, angle=0.))

    # Inner Rings - Quads
    inner_endcap_layers.append(DetectorElement(Point(263, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(291, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(322, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(357, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(396, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(437, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(486, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(543, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(604, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(675, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(749, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(835, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(925, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1026, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1142, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1272, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1403, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1553, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1721, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(1909, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(2120, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(2357, 100.1), height=42, width=4, angle=0.))
    inner_endcap_layers.append(DetectorElement(Point(2621, 100.1), height=42, width=4, angle=0.))
#    inner_endcap_layers.append(DetectorElement(Point(2357, 104.07), height=35.63, width=4, angle=0.))
#    inner_endcap_layers.append(DetectorElement(Point(2621, 108.8), height=25.86, width=4, angle=0.))
    
    for layer in inner_endcap_layers:
        simmetric_layer = DetectorElement(Point(-layer.center[0], layer.center[1]), layer.height, layer.width)
        layer.graph.SetFillColorAlpha(38, 0.8)
        simmetric_layer.graph.SetFillColorAlpha(38, 0.8)
        pixelDetector.addElement(layer)
        pixelDetector.addElement(simmetric_layer)

    # Outer Endcap
    outer_endcap_layers = []
    # Layer 2
    outer_endcap_layers.append(DetectorElement(Point(1145.5, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1249, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1364.5, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1491.5, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1632.5, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1789, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1961, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2151, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2361, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2593, 174.6), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2850, 174.6), height=41.4, width=17, angle=0.))

    # Layer 3
    outer_endcap_layers.append(DetectorElement(Point(1145.5, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1297, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1473, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1676, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1910, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2180, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2491, 234.65), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2850, 234.65), height=41.4, width=17, angle=0.))

    # Layer 4
    outer_endcap_layers.append(DetectorElement(Point(1145.5, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1277, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1427, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1597, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(1789, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2007, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2253, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2533, 294.7), height=41.4, width=17, angle=0.))
    outer_endcap_layers.append(DetectorElement(Point(2850, 294.7), height=41.4, width=17, angle=0.))
    
    for layer in outer_endcap_layers:
        simmetric_layer = DetectorElement(Point(-layer.center[0], layer.center[1]), layer.height, layer.width)
        layer.graph.SetFillColorAlpha(38, 0.8)
        simmetric_layer.graph.SetFillColorAlpha(38, 0.8)
        pixelDetector.addElement(layer)
        pixelDetector.addElement(simmetric_layer)

    # Outer Barrel Inclined
    outer_barrel_layers = []
    # Inclined L2
    outer_barrel_layers.append(DetectorElement(Point(404.684, 168.468), height=41.7, width=17, angle=90. - 67.))
    outer_barrel_layers.append(DetectorElement(Point(483.284, 168.468), height=41.7, width=17, angle=90. - 67.))
    outer_barrel_layers.append(DetectorElement(Point(580.884, 168.468), height=41.7, width=17, angle=90. - 67.))
    outer_barrel_layers.append(DetectorElement(Point(702.084, 168.468), height=41.7, width=17, angle=90. - 67.))
    outer_barrel_layers.append(DetectorElement(Point(852.384, 168.468), height=41.7, width=17, angle=90. - 67.))
    outer_barrel_layers.append(DetectorElement(Point(1039.085, 168.468), height=41.7, width=17, angle=90. - 67.))
    
    # Inclined L3
    outer_barrel_layers.append(DetectorElement(Point(400.488, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(458.588, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(525.188, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(601.588, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(689.088, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(789.388, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(904.388, 235.014), height=41.7, width=17, angle=90. - 58.))
    outer_barrel_layers.append(DetectorElement(Point(1036.285, 235.014), height=41.7, width=17, angle=90. - 58.))

    # Inclined L4
    outer_barrel_layers.append(DetectorElement(Point(397.368, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(450.068, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(508.868, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(574.468, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(647.568, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(729.268, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(820.368, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(921.968, 297.392), height=41.7, width=17, angle=90. - 55.))
    outer_barrel_layers.append(DetectorElement(Point(1035.365, 297.392), height=41.7, width=17, angle=90. - 55.))
    
    for layer in outer_barrel_layers:
        simmetric_layer = DetectorElement(Point(-layer.center[0], layer.center[1]), layer.height, layer.width, -layer.angle)
        layer.graph.SetFillColorAlpha(38, 0.8)
        simmetric_layer.graph.SetFillColorAlpha(38, 0.8)
        pixelDetector.addElement(layer)
        pixelDetector.addElement(simmetric_layer)
    
    return pixelDetector

