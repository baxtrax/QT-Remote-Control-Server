# NOTICE
This repo is archived. A newer version of this software was developed. Please see the Version 2 (V2) [here](https://github.com/baxtrax/QT-Remote-Control-Client_V2).

# QT Remote Control Server

This is socket application that is ment to be paired with its QT counter-part [here](https://github.com/baxtrax/QT-Remote-Control-Server). The raspberrypi will communicate with a client via UDP socket and then send movement data over serial to a respective arduino sheild. A sheild was used because generating 4 different PWM signals of reliable frequency was difficult because the raspberrypi only has 2 built in PWM channels. This also allows for the use of external stepper libraries such as AccelStepper which allows acceleration and deceleration. 

This software is one tiny part of the main robot. There are Driver boards, USB Wifi adaptars, and other electronics that makes the whole robot possible.

## Details

This section will show current features of the application. There will not be any pictures because it is a purely console based application

### Features
* Steps each motor using DFRobot arduino sheild.
* Microstepping
* Packet validitity checking

More details of how parts of this program work and why design decisions where made can be found on this repositorys respective wiki.

## Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/) - The main programming language used
* [Raspberry Pi B3+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) - Current Embedded Systems running the server

## Authors

* **Bradley G** - *Original Creator* - [Baxtrax](https://github.com/baxtrax)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
