
class Range1D:
    def __init__(self,
                 lowerBound: float,
                 upperBound: float):
        self.lowerBound = lowerBound
        self.upperBound = upperBound

    def minimum(self) -> float:
        return self.lowerBound

    def maximum(self) -> float:
        return self.upperBound
