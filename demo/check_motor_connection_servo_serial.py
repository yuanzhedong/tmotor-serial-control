from tmotor_serial_control import TMotorManager

Type = 'AK8-64'
ID = 0

with TMotorManager() as manager:
    if manager.check_connection():
        print("\nmotor is successfully connected!\n")
    else:
        print("\nmotor not connected.\n")
    
