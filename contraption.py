"""This class will create LED functions for use on a web-based application."""

from gpiozero import LED
from time import sleep


class PiLedContraption:

    _led_ports = []

    def __init__(self):

        self._led_ports = [18, 23, 25, 12, 16, 20, 21, 26, 19, 13]


    def led_on(self, led_index):

        if not 0 <= led_index < 10:
            print("{} is not a valid LED index".format(led_index))
        else:
            print("LED {} is on.".format(led_index))
            LED(self._led_ports[led_index]).on()
            #self._led_ports[led_index] = 1

    def led_off(self, led_index):

        if not 0 <= led_index < 10:
            print("{} is not a valid LED index".format(led_index))
        else:
            print("LED {} is on.".format(led_index))
            LED(self._led_ports[led_index]).off()
            #self._led_ports[led_index] = 0

    '''
    def race_up(self):
        for i in led_ports:
            blink_led_once(blink_frequency, i)
            # print("Activating port ", i)

    def race_down(self):
        
        for i in led_ports:
            blink_led_once(blink_frequency, reversed(i))
            # print("Activating port ", reversed(i))
            
        '''

    def dance_randomly(self):
        pass

if __name__ == "__main__":
    test = PiLedContraption()
    print(type(test))

    print("\nTesting LED 0")
    test.led_on(0)

    '''print("\nTesting LED 0 off")
    test.led_off(2)

    print("\nTesting invalid LED on")
    test.led_on(10)

    print("\nTesting invalid LED off")
    test.led_off(10)

    print("\nTesting LED 1")
    test.led_on(1)

    print("\nTesting LED 1 off")
    test.led_off(2)'''


