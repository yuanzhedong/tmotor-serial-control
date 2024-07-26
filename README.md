

# Setup the motor hardware

Follow this [doc](https://docs.google.com/document/d/15epu72rCWf0Awd0_fC8zYKfM3MxYQvvjvQTrm07DAhM/edit?usp=sharing) to setup the connection between host machine and motor via rlink

# Send control cmd to motor via serial

```
conda create --name tmotor-serial-control python=3.8
conda activate tmotor-serial-control
pip install -e .
python demo/check_motor_connection_servo_serial.py # check connection
python demo/demo_pv_servo_serial.py # set position and velocity
```