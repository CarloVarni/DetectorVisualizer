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
    
    # Get The seeds
    grs = []
    seeds = []
    with open('seeds.txt', 'r') as inFile:
        for line in inFile:
            [b_z, b_r, m_z, m_r, t_z, t_r] = re.findall('seed: \[(.*), (.*)\] \[(.*), (.*)\] \[(.*), (.*)\]', line)[0]            
            gr = TGraph()
            gr.SetPoint(0, float(b_z), float(b_r))
            gr.SetPoint(1, float(m_z), float(m_r))
            gr.SetPoint(2, float(t_z), float(t_r))
            gr.SetMarkerColor(2)
            gr.SetMarkerStyle(20)
            gr.SetLineColor(2)
            gr.SetMarkerSize(0.4)
            grs.append(gr)

    grs = grs[:4]
            
    canvas = TCanvas()
    canvas.SetTicks()
    pixels.draw(canvas)
    strips.draw(canvas, "SAME")
    
    # Pseudo-Rapidity Lines
    line_eta = TLine()
    line_eta.SetLineStyle(3)
    line_eta.SetLineColorAlpha(4, 1)
    # eta = 1
    line_eta.DrawLine( 0, 0, rangeR.maximum()/math.tan(0.704774), rangeR.maximum() )
    line_eta.DrawLine( 0, 0, -rangeR.maximum()/math.tan(0.704774), rangeR.maximum() )
    # eta = 2
    line_eta.DrawLine( 0, 0, rangeR.maximum()/math.tan(0.268779), rangeR.maximum() )
    line_eta.DrawLine( 0, 0, -rangeR.maximum()/math.tan(0.268779), rangeR.maximum() )
    # eta = 3
    line_eta.DrawLine( 0, 0, rangeZ.maximum(), rangeZ.maximum() * math.tan(0.0987791))
    line_eta.DrawLine( 0, 0, -rangeZ.maximum(), rangeZ.maximum() * math.tan(0.0987791))
    # eta = 4
    line_eta.DrawLine( 0, 0, rangeZ.maximum(), rangeZ.maximum() * math.tan(0.0357791))
    line_eta.DrawLine( 0, 0, -rangeZ.maximum(), rangeZ.maximum() * math.tan(0.0357791))

    for gr in grs:
        gr.Draw("PLSAME")
    grid.draw(canvas, rangeR)
    canvas.Draw()
    canvas.SaveAs("PixelDetector.pdf")
    canvas.SaveAs("PixelDetector.png")
    
