
def main():
    from core.Range1D import Range1D
    from core.Point import Point
    from core.Grid import Grid
    from core.DetectorElement import DetectorElement
    from core.Detector import Detector
    
    from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex
    
    from examples.ITkPixelDetector import ITkPixelDetector
    from examples.ITkStripDetector import ITkStripDetector
    from examples.HgtdDetector import HgtdDetector
    
    import math
    import re
    
    pixelGridBoundaries = [-3000, -2700, -2500, -1400, -925, -450, -250, 250, 450, 925, 1400, 2500, 2700, 3000]

    rangeR = Range1D(0, 400)
    rangeZ = Range1D(pixelGridBoundaries[0], pixelGridBoundaries[len(pixelGridBoundaries) - 1])
    rangeInclusive = Range1D(-4000, 4000)
    
    grid = Grid(pixelGridBoundaries)
    detectors = [
        ITkPixelDetector(rangeR, rangeZ, rangeInclusive),
#        ITkStripDetector(rangeR, rangeZ, rangeInclusive),
#        HgtdDetector(rangeR, rangeZ, rangeInclusive)
    ]

    validityRangesMiddle = [
        (0, 0),
        (40, 90),
        (40, 200),
        (46, 200),
        (46, 200),
        (46, 250),
        (46, 250),
        (46, 250),
        (46, 200),
        (46, 200),
        (40, 200),
        (40, 90),
        (0, 0)
    ]
    assert len(validityRangesMiddle) == len(pixelGridBoundaries) - 1
    validityRangeGraph = []

    for i in range(0, len(validityRangesMiddle)):
        (rmin, rmax) = validityRangesMiddle[i]
        zmin = pixelGridBoundaries[i]
        zmax = pixelGridBoundaries[i + 1]

        gr = TGraph()
        gr.SetFillColorAlpha(2, 0.5)
        gr.SetPoint(0, zmin, rmin)
        gr.SetPoint(1, zmax, rmin)
        gr.SetPoint(2, zmax, rmax)
        gr.SetPoint(3, zmin, rmax)
        gr.SetPoint(4, zmin, rmin)
        validityRangeGraph.append(gr)
        
    canvas = TCanvas("canvas", "canvas")
    canvas.SetTicks()
    for i in range(0, len(detectors)):
        if i == 0:
            detectors[i].draw(canvas)
        else:
            detectors[i].draw(canvas, "SAME")
    
    # Pseudo-Rapidity Lines
    line_eta = TLine()
    line_eta.SetLineStyle(3)
    line_eta.SetLineColorAlpha(4, 1)

    latex = TLatex()
                
    # [eta 1, eta 2, eta 3, eta 4]
    thetas = [0.704774, 0.268779, 0.0987791, 0.0357791]
    etas = [1, 2, 3, 4]
    for i in range(0, len(thetas)):
        theta = thetas[i]
        eta = etas[i]

        y_value_atLimitZ = math.tan(theta) * rangeZ.maximum()
        x_value_atLimitR = rangeR.maximum()/math.tan(theta)

        if x_value_atLimitR < rangeZ.maximum():
            line_eta.DrawLine( 0, 0, x_value_atLimitR, rangeR.maximum() )
            line_eta.DrawLine( 0, 0, -x_value_atLimitR, rangeR.maximum() )
            text = "#scale[0.5]{#color[4]{#eta = " + str(eta) + "}}"
            latex.DrawLatex( x_value_atLimitR, 1.02 * rangeR.maximum(), text)
            latex.DrawLatex( - x_value_atLimitR, 1.02 * rangeR.maximum(), text)
        else:
            line_eta.DrawLine( 0, 0, rangeZ.maximum(), y_value_atLimitZ)
            line_eta.DrawLine( 0, 0, -rangeZ.maximum(), y_value_atLimitZ)
            text = "#scale[0.5]{#color[4]{#eta = " + str(eta) + "}}"
            latex.DrawLatex( 1.05 * rangeZ.maximum(), y_value_atLimitZ, text)
            latex.DrawLatex( 1.15 * rangeZ.minimum(), y_value_atLimitZ, text)
            
    grid.draw(canvas, rangeR)

    for gr in validityRangeGraph:
        gr.Draw("F SAME")

    canvas.Draw()
    canvas.SaveAs("PixelDetector.pdf")
    canvas.SaveAs("PixelDetector.png")
    
if __name__ == "__main__":
    main()
