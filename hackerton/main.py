import motor, runloop, force_sensor
from hub import port,button
import color
import color_sensor

num = 1
flag=1
motor_running = False

motor.run_for_degrees(port.C, -100, 360)

async def main():
    global num,flag
    while True:
        force = force_sensor.force(port.B)

        if force_sensor.force(port.B) > 0:
            num *= -1
            await motor.run_for_degrees(port.D, 620* num , 360)

        if button.pressed(button.LEFT):
            motor.run_for_degrees(port.C, 100, 360)

        elif color_sensor.color(port.E) == color.YELLOW:
            motor.run_for_degrees(port.C, -100 , 360)

        if button.pressed(button.RIGHT):
            flag*=-1
            await motor.run_for_degrees(port.F,250*flag,240)

runloop.run(main())