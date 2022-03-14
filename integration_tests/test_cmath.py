from cmath import (exp, log, sqrt, acos, asin, atan, cos, sin, tan,
                   acosh, asinh, atanh, cosh, sinh, tanh)
from ltypes import c64

def test_power_logarithmic():
    x: c64
    y: c64
    x = complex(3, 3)
    y = exp(x)
    y = log(x)
    y = sqrt(x)


def test_trigonometric():
    x: c64
    y: c64
    x = complex(3, 3)
    y = acos(x)
    y = asin(x)
    y = atan(x)
    y = cos(x)
    y = sin(x)
    y = tan(x)


def test_hyperbolic():
    x: c64
    y: c64
    x = complex(3, 3)
    y = acosh(x)
    y = asinh(x)
    y = atanh(x)
    y = cosh(x)
    y = sinh(x)
    y = tanh(x)


test_power_logarithmic()
test_trigonometric()
test_hyperbolic()
