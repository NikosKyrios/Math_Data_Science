"""Placeholder for image transformation examples using NumPy."""
import numpy as np

def rotate_point(x, y, theta):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s],[s, c]])
    return R.dot(np.array([x,y]))

if __name__ == "__main__":
    print(rotate_point(1,0,np.pi/2))
