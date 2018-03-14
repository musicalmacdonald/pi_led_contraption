"""This class will create LED functions for use on a web-based application."""

from gpiozero import LED
from time import sleep


class PiLedContraption:

    _led_ports = []
    _leds = []
    _led_index_array = []

    def __init__(self):

        self._led_ports = [18, 23, 25, 12, 16, 20, 21, 26, 19, 13]
        for i in self._led_ports:
            self._leds.append(LED(i))
        self._led_index_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._st = .2

    def led_on(self, led_index):
        if not 0 <= led_index < 10:
            print("{} is not a valid LED index".format(led_index))
        else:
            print("LED {} is on.".format(led_index))
            self._leds[led_index].on()
            #self._led_ports[led_index] = 1

    def led_off(self, led_index):
        if not 0 <= led_index < 10:
            print("{} is not a valid LED index".format(led_index))
        else:
            print("LED {} is on.".format(led_index))
            self._leds[led_index].off()
            #self._led_ports[led_index] = 0

    def race_up(self):
        for i in self._led_index_array:
            self.led_on(i)
            sleep(self._st)
            self.led_off(i)
            # print("Activating port ", i)

    '''def race_down(self):
        
        for i in _leds:
            blink_led_once(blink_frequency, reversed(i))
            # print("Activating port ", reversed(i))'''


    def dance_randomly(self):
        pass


if __name__ == "__main__":
    #test class initiation
    test = PiLedContraption()
    print(type(test))

    #test on/off
    print("\nTesting LED 0")
    test.led_on(0)
    sleep(.5)

    print("\nTesting LED 0 off")
    test.led_off(0)
    sleep(.5)

    print("\nTesting invalid LED on")
    test.led_on(10)
    sleep(.5)

    #race up/ race down
    print ("Testing race up")
    test.race_up()
    print ("Testing race down")
    test.race_down()




