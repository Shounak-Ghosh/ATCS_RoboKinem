import numpy as np
import math
import ex_32




def main():
    print()
    """
    Main function
    """
    t_ab = np.array(
        [[1 / 2 ** .5, -1 / 2 ** .5, 0, -1], [1 / 2 ** .5, 1 / 2 ** .5, 0, 0],
         [0, 0, 1, 1], [0, 0, 0, 1]])

    t_cb = np.array([[1 / 2 ** .5, 0, 1 / 2 ** .5, 0], [0, 1, 0, 1],
                     [-1 / 2 ** .5, 0, 1 / 2 ** .5, 0], [0, 0, 0, 1]])
    t_ba = np.linalg.inv(t_ab)
    t_ca = t_cb * t_ba
    print("\npart (c)")
    print(t_ca) 


if __name__ == '__main__':
    main()
