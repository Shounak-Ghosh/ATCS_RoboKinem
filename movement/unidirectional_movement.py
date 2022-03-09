import mecanum_wheel_movement as drive
import argparse
import time
import math
import os
import sys

script_dir = os.path.dirname(__file__)
simulation_dir = os.path.join(script_dir, '..', 'simulation')
sys.path.append(simulation_dir)
import circle as c
import shapes as sh
import spline as sp


def move_shape(point_list):
    for i in range(len(point_list) - 1):
        x_dist = point_list[i + 1][0] - point_list[i][0]
        y_dist = point_list[i + 1][1] - point_list[i][1]

        vector_length = math.sqrt(x_dist ** 2 + y_dist ** 2)
        if vector_length != 0:
            scale = 50 / vector_length
        else:
            scale = 1
        x_dist *= scale
        y_dist *= scale
        drive.move_vector(x_dist, y_dist, 0)
        time.sleep(.03)
    drive.stop_car()


def main(path):
    match path:
        case 0:
            c_scale = 2000  # scale because number of points is fixed to 360
            circle_point_list = c.generate_circle([-c_scale, 0], [c_scale, 0])
            move_shape(circle_point_list)
        case 1:
            loop_point_list = sh.generate_loop([1, 1], [-1, 1], [-1, -1],
                                               [1, -1])
            diagonal_loop_point_list = sh.generate_loop([1, 0], [0, 1], [-1, 0],
                                                        [0, -1])
            move_shape(loop_point_list)
        case 2:
            spline_point_list = sp.generate_spline([[0, 1], [1, 3], [2, 2]])
            move_shape(spline_point_list)


if __name__ == '__main__':
    parser.add_argument("-p", "--path",
                        help="0 for circle, 1 for loop, 2 for spline",
                        type=int,
                        default=1)
    args = parser.parse_args()
    try:
        main(args.path)
    except KeyboardInterrupt:
        drive.stop_car()  # stop movement
        drive.destroy()  # clean up GPIO
        print("\nStopped and cleanup done")
