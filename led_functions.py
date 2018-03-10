from gpiozero import LED
from time import sleep


def blink_led_once(blink_frequency, port):
    """turns the led on for 1/2 the time specified in blink_frequency, then it off for the same amount of time."""
    myLED = LED(port)

    myLED.on()
    sleep(blink_frequency / 2)
    myLED.off()
    sleep(blink_frequency / 2)


def blink_led_forever(port):
    """blink the led once per second in a never ending loop"""
    while True:
        blink_led_once(1, port)


def race_led_up(blink_frequency):

    led_ports = [18, 23, 25, 12, 16, 20, 21, 26, 19, 13]

    for i in led_ports:
        blink_led_once(blink_frequency, led_ports[i])
    '''
    # led 1
    blink_led_once(blink_frequency, 18)
    # led 2
    blink_led_once(blink_frequency, 23)
    # led 3
    blink_led_once(blink_frequency, 25)
    # led 4
    blink_led_once(blink_frequency, 12)
    # led 5
    blink_led_once(blink_frequency, 16)
    # led 6
    blink_led_once(blink_frequency, 20)
    # led 7
    blink_led_once(blink_frequency, 21)
    # led 8
    blink_led_once(blink_frequency, 26)
    # led 9
    blink_led_once(blink_frequency, 19)
    # led 10
    blink_led_once(blink_frequency, 13)
    '''
    

def race_led_down(blink_frequency):

    led_ports = [18, 23, 25, 12, 16, 20, 21, 26, 19, 13]

    for i in led_ports:
            blink_led_once(blink_frequency, led_ports[::-i])


def test_leds():
    print("This will make the LED blink once")
    blink_led_once(2, 18)

    print("This will make them race")
    race_led_up(1)
    race_led_down(1)

    print("Come on, we can go faster!")
    race_led_up(.5)


if __name__ == "__main__":
    test_leds()
