from machine import Pin, Timer


def main():
    led = Pin("LED", Pin.OUT)
    Timer().init(freq=1, mode=Timer.PERIODIC, callback=lambda _: led.toggle())


if __name__ == "__main__":
    main()
