import numpy as np

from mixem.distribution.distribution import Distribution


class SimpleDistribution(Distribution):
    def __init__(self, f_density, f_estimate_parameters):
        self.f_density = f_density,
        self.f_estimate_parameters = f_estimate_parameters

    def density(self, *args, **kwargs):
        return self.f_density(*args, **kwargs)
 
    def estimate_parameters(self, *args, **kwargs):
        return self.f_estimate_parameters(*args, **kwargs)