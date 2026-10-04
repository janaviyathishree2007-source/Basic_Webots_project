"""my_controller_one_last_try_pleaseeee controller."""

from controller import Robot


def main():
    robot = Robot()
    time_step = int(robot.getBasicTimeStep())

    max_speed = 3.0
    # Threshold calibrated above background noise (~70-75)
    wall_threshold = 85.0

    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')

    if left_motor is None or right_motor is None:
        print("ERROR: Wheel motors not found.")
        return

    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    proximity_sensors = []
    for i in range(8):
        sensor = robot.getDevice(f'ps{i}')
        if sensor is None:
            print(f"ERROR: Distance sensor ps{i} not found.")
            return
        sensor.enable(time_step)
        proximity_sensors.append(sensor)

    print("Controller started successfully.")

    while robot.step(time_step) != -1:
        ps_values = [s.getValue() for s in proximity_sensors]

        # Key sensor indices:
        # ps0: Front-Right | ps7: Front-Left | ps5: Left-Side
        front_obstacle = ps_values[0] > wall_threshold or ps_values[7] > wall_threshold
        left_wall = ps_values[5] > wall_threshold

        if front_obstacle:
            # Wall ahead: turn right on the spot
            left_speed = max_speed
            right_speed = -max_speed
        elif left_wall:
            # Wall detected on left: proceed straight
            left_speed = max_speed
            right_speed = max_speed
        else:
            # No wall on left: curve left gradually to hug corners/find walls
            left_speed = max_speed * 0.5
            right_speed = max_speed

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


if __name__ == '__main__':
    main()