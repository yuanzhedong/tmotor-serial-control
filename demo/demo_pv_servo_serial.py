from tmotor_serial_control.servo_serial import *
from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop

pos=1
print(pos)
vel=7

with TMotorManager(port = '/dev/ttyUSB0', baud=961200, motor_params=Servo_Params_Serial['AK80-64']) as dev:
        loop = SoftRealtimeLoop(dt=0.005, report=True, fade=0.0)
        dev.set_zero_position()
        dev.update()
        
        dev.enter_position_velocity_control()

        send_cmd = True
        for t in loop:
                dev.set_output_angle_radians(pos, vel)
                dev.update(send_cmd)
                #breakpoint()
                send_cmd = True
                #print(f"\r {dev}", end='')
                print(f"\r {dev}")
        
