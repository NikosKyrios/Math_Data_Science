"""Derivative exploration placeholder (kept from original outline)."""
import numpy as np

def derivative(f, x, h=1e-6):
    return (f(x+h)-f(x-h)) / (2*h)

if __name__ == "__main__":
    print(derivative(lambda x: x**2, 3.0))
