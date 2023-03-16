from core.Range1D import Range1D
from ROOT import TCanvas, TLatex, TLine

class Grid:
    def __init__(self,
                 boundaries: list):
        self.boundaries = boundaries
        
    def draw(self,
             canvas: TCanvas,
             floorCeiling: Range1D):

        for i in range(0, len(self.boundaries)):
            val = self.boundaries[i]

            line = TLine()
            line.SetLineStyle(2)
            line.DrawLine(val, floorCeiling.minimum(), val, floorCeiling.maximum())
            
            if i == len(self.boundaries) - 1:
                continue
            
            latex = TLatex()
            position = self.boundaries[i] + 0.35 * (self.boundaries[i+1] - self.boundaries[i])
            latex.SetTextSize(0.015);
            latex.DrawLatex(position, 0.95 * floorCeiling.maximum(), f"#{i+1}")
