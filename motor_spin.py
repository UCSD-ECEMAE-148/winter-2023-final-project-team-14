import time
import sys

class VESC:
    def __init__(self, serial_port, percent=.2, has_sensor=False, start_heartbeat=True, baudrate=115200, timeout=0.05, steering_scale = 0.5, steering_offset = 0.6):
        try:
            import pyvesc
        except Exception as err:
            print("\n\n\n\n", err, "\n")
            print("please use the following command to import pyvesc so that you can also set")
            print("the servo position:")
            print("pip install git+https://github.com/LiamBindle/PyVESC.git@master")
            print("\n\n\n")
            time.sleep(1)
            raise
        assert percent <= 1 and percent >= -1,'\n\nOnly percentages for MAX_VESC_SPEED (recommend .2) (negative values flip direction of motor)'
        self.steering_scale = steering_scale
        self.steering_offset = steering_offset
        self.percent = percent
        try:
            self.v = pyvesc.VESC(serial_port, has_sensor, start_heartbeat, baudrate, timeout)
        except Exception as err:
            print("\n\n\n\n", err)
            print("\n\nto fix permission denied errors, try running the following command:")
            print("sudo chmod a+rw {}".format(serial_port), "\n\n\n\n")
            time.sleep(1)
            raise

    def run(self, angle, throttle):
        self.v.set_servo((angle * self.steering_scale) + self.steering_offset)
        self.v.set_duty_cycle(throttle*self.percent)

    #Throttle is range [0,1], move_time is in seconds
    def move(self, throttle, move_time):
        self.v.set_duty_cycle(throttle * self.percent)
        time.sleep(move_time)
        self.v.set_rpm(0)

    def turn(self, angle):
        self.v.set_servo((angle * self.steering_scale) + self.steering_offset)

if __name__ == '__main__':
    vesc = VESC("/dev/ttyACM0")
    #vesc.turn(20)
    #time.sleep(1)
    #vesc.move(0.1, 2)
    vesc.run(20, 0.2)
    time.sleep(2)
    vesc.run(-20, 0.2)
    sys.exit()
