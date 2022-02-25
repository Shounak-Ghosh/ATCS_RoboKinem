import time
import mecanum_wheel_movement.py as drive

ROBOT_LENGTH = 1
ROBOT_WIDTH = 1


def move_vector(x, y, w):
    w1 = y - x + w * (ROBOT_LENGTH + ROBOT_WIDTH)
    w2 = y + x - w * (ROBOT_LENGTH + ROBOT_WIDTH)
    w3 = y - x - w * (ROBOT_LENGTH + ROBOT_WIDTH)
    w4 = y + x + w * (ROBOT_LENGTH + ROBOT_WIDTH)

    # scale to ensure largest movement value is 100
    # ex. if w1 is largest, w1/(w1/100) = 100
    scale = max(max(w1, w2, w3, w4), abs(min(w1, w2, w3, w4)))
    if scale > 1:
        w1 /= scale / 100
        w2 /= scale / 100
        w3 /= scale / 100
        w4 /= scale / 100

    print(w1, w2, w3, w4)

    drive.fr.move(w1)
    drive.fl.move(w2)
    drive.fl.move(w3)
    drive.rr.move(w4)


def main():
    n = 360
    for i in range(n):
        x = np.cos(i * np.pi / 180)  # converting degrees to radians
        y = np.sin(i * np.pi / 180)
        move_vector(x, y, 0)
        time.sleep(.01)

    drive.stop_car()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        drive.stop_car()  # stop movement
        drive.destroy()  # clean up GPIO
        print("\nStopped and cleanup done")
