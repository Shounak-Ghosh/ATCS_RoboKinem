import numpy as np
def rot_x(theta):
    rot = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta), np.cos(theta)]])
    return rot

def main():
    print(rot_x(np.radians(90)))

if __name__ == '__main__':
    main()