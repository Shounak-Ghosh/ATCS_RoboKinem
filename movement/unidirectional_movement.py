import time
import mecanum_wheel_movement.py as drive
script_dir = os.path.dirname(__file__)
simulation_dir = os.path.join(script_dir, '..', 'simulation')
sys.path.append(simulation_dir)
import circle as c
import loop as l




def move_shape(point_list):
    for i in range(len(point_list) - 1):
        x_dist = point_list[i + 1][0] - point_list[i][0]
        y_dist = point_list[i + 1][1] - point_list[i][1]
        drive.move_vector(x_dist, y_dist, 0)
        time.sleep(.03)
    drive.stop_car()


def main():
    circle_point_list = c.generate_circle([-1, 0], [1, 0])
    move_shape(circle_point_list)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        drive.stop_car()  # stop movement
        drive.destroy()  # clean up GPIO
        print("\nStopped and cleanup done")
