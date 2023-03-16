from core.Range1D import Range1D
from core.Point import Point
from core.Grid import Grid
from core.DetectorElement import DetectorElement
from core.Detector import Detector

from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex

from examples.ITkPixelDetector import ITkPixelDetector
from examples.ITkStripDetector import ITkStripDetector

if __name__ == "__main__":
    import math
    import re
    
    pixelGridBoundaries = [-3000, -2500, -1400, -925, -450, -250, 250, 450, 925, 1400, 2500, 3000]

    rangeR = Range1D(0, 1100)
    rangeZ = Range1D(pixelGridBoundaries[0], pixelGridBoundaries[len(pixelGridBoundaries) - 1])
    rangeInclusive = Range1D(-4000, 4000)
    
    grid = Grid(pixelGridBoundaries)
    pixels = ITkPixelDetector(rangeR, rangeZ, rangeInclusive) #
    strips = ITkStripDetector(rangeR, rangeZ, rangeInclusive) #
                
    canvas = TCanvas("canvas", "canvas")
    canvas.SetTicks()
    pixels.draw(canvas)
    strips.draw(canvas, "SAME")
    
    # Pseudo-Rapidity Lines
    line_eta = TLine()
    line_eta.SetLineStyle(3)
    line_eta.SetLineColorAlpha(4, 1)

    # [eta 1, eta 2, eta 3, eta 4]
    for theta in [0.704774, 0.268779, 0.0987791, 0.0357791]:        
        y_value_atLimitZ = math.tan(theta) * rangeZ.maximum()
        x_value_atLimitR = rangeR.maximum()/math.tan(theta)

        if x_value_atLimitR < rangeZ.maximum():
            line_eta.DrawLine( 0, 0, x_value_atLimitR, rangeR.maximum() )
            line_eta.DrawLine( 0, 0, -x_value_atLimitR, rangeR.maximum() )
        else:
            line_eta.DrawLine( 0, 0, rangeZ.maximum(), y_value_atLimitZ)
            line_eta.DrawLine( 0, 0, -rangeZ.maximum(), y_value_atLimitZ)
        
    grid.draw(canvas, rangeR)
    canvas.Draw()
    canvas.SaveAs("PixelDetector.pdf")
    canvas.SaveAs("PixelDetector.png")
    
