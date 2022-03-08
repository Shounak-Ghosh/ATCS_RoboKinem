import mecanum_wheel_movement as drive
import time
import math
import os
import sys
script_dir = os.path.dirname(__file__)
simulation_dir = os.path.join(script_dir, '..', 'simulation')
sys.path.append(simulation_dir)
import circle as c
import shapes as s


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


def main():
    c_scale = 2000
    circle_point_list = c.generate_circle([-c_scale, 0], [c_scale, 0])
    l_scale = 1
    loop_point_list = s.generate_loop([1, 1], [-1, 1], [-1, -1], [1, -1])
    diagonal_loop_point_list = s.generate_loop([l_scale, 0], [0, l_scale], [-l_scale, 0], [0, -l_scale])
    move_shape(loop_point_list)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        drive.stop_car()  # stop movement
        drive.destroy()  # clean up GPIO
        print("\nStopped and cleanup done")
