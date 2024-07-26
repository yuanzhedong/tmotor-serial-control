from tmotor_serial_control.servo_serial import *
from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop

pos=np.sin(1)/2
vel=6

with TMotorManager(port = '/dev/ttyUSB0', baud=961200, motor_params=Servo_Params_Serial['AK80-64']) as dev:
        loop = SoftRealtimeLoop(dt=0.005, report=True, fade=0.0)
        dev.set_zero_position()
        dev.update()
        
        dev.enter_position_velocity_control()
        
        for t in loop:
            dev.set_output_angle_radians(pos, vel)
            dev.update()
            #print(f"\r {dev}", end='')
            print(f"\r {dev}")
        
