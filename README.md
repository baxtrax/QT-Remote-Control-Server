# QT Remote Control Server

This is socket application that is ment to be paired with its QT counter-part [here](https://github.com/baxtrax/QT-Remote-Control-Server). This is uses basic threading to allow multiple steppers to be stepped at once. Using this paired with a custom PCB and 4 DRV8825's, allows the GPIO of a raspberry pi to communicate and control stepper motor direction, speed, etc.

This software is one tiny part of the main robot. There are Driver boards, USB Wifi adaptars, and other electronics that makes the whole robot possible.

## Details

This section will show current features of the application. There will not be any pictures because it is a purely console based application

### Features
* Steps each indivual motor using indiviual threading and queues
* Microstepping (Coming soon!)
* Packet validitity checking

More details of how parts of this program work and why design decisions where made can be found on this repositorys respective wiki.

## Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/) - The main programming language used
* [Raspberry Pi B3+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) - Current Embedded Systems running the server

## Authors

* **Bradley G** - *Original Creator* - [Baxtrax](https://github.com/baxtrax)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
