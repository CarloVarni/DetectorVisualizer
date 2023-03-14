from core.Range1D import Range1D
from core.Point import Point
from core.Grid import Grid
from core.DetectorElement import DetectorElement
from core.Detector import Detector

from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex

from examples.ITkPixelDetector import ITkPixelDetector

if __name__ == "__main__":
    pixelGridBoundaries = [-3000, -2500, -1400, -925, -450, -250, 250, 450, 925, 1400, 2500, 3000]

    rangeR = Range1D(0, 350)
    rangeZ = Range1D(pixelGridBoundaries[0], pixelGridBoundaries[len(pixelGridBoundaries) - 1])
    rangeInclusive = Range1D(-4000, 4000)
    
    grid = Grid(pixelGridBoundaries)
    pixels = ITkPixelDetector(rangeR, rangeZ, rangeInclusive)
    
    canvas = TCanvas()
    canvas.SetTicks()
    pixels.draw(canvas)
    grid.draw(canvas, Range1D(0, 350))
    canvas.Draw()
    canvas.SaveAs("PixelDetector.pdf")
    
