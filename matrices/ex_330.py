from cmath import pi
import math
import numpy as np

#main function
def main():
    print("part a: case a: ")
    print("theta=", "1,","(w,v)=\n",np.array([[0,0,0],[0,0,1]]).transpose())
    print("part a: case b: ")
    print("theta=", "1,","(w,v)=\n",np.array([[0,0,math.pi],[0,0,1]]).transpose())
    print("part b: case a: ")
    print("theta=", "1,","(w,v)=\n",np.array([[0,0,0],[0,0,1]]).transpose())
    print("part b: case b: ")
    print("theta=", "pi/2,","(w,v)=\n",np.array([[0,0,math.pi],[0,0,2/math.pi]]).transpose())

if __name__ == '__main__':
    main()
