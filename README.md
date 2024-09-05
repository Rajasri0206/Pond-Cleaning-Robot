# Pond-Cleaning-Robot
 This project involves the development of a real-time Bluetooth-controlled robotic pond cleaner that autonomously detects and collects waste using various sensors.
# Project overview
This project aims to develop an automated system for cleaning ponds using a robotic device controlled via Bluetooth. The system integrates various sensors such as the MQ2 gas (smell) sensor and a PIR motion sensor to detect waste in the pond. The cleaner uses motors for movement and a robotic arm to collect waste automatically or manually, based on user input via a Bluetooth-connected mobile device. This project showcases the potential for automating environmental cleaning tasks using low-cost, open-source microcontrollers like the Raspberry Pi Pico.
# Key skills 
* Microcontroller Programming(Micro Python)
* Sensors Integration
* Motor Control
* Robotics
* Bluetooth Communication
* Embedded Systems
* LCD Display
# Key Features
1. Automatic Waste Detection:
   * MQ2 sensor detects the smell of waste.
   * PIR sensor detects the physical presence of objects or waste.
2. Bluetooth Control:
   * Cleaner movement and robotic arm control can be managed via a mobile device.
3. Robotic Arm for Waste Collection:
   * Automatically collects waste when the PIR sensor detects it.
   * Can be manually controlled using Bluetooth commands for fine adjustments.
4. Real-Time Feedback:
   * LCD displays the status of sensors and operational states (e.g., "Smell: ON" or "PIR: OFF").
5. Manual or Automatic Control:
   * Users can manually control the robot to a specific location via Bluetooth commands.
   * The robot can automatically collect waste when detected by the sensors.
# Components
* Raspberry Pi Pico: Central microcontroller for handling all system components.
* MQ2 Gas Sensor: Used to detect the smell of waste in the pond.
* PIR Motion Sensor: Detects the presence of objects or waste.
* L293D Motor Driver: Controls the motors responsible for the cleaner's movement.
* Motors (2x): Used for the movement of the cleaner in various directions.
* Robotic Arm: Automates waste collection by picking up and releasing waste.
* HC-05 Bluetooth Module: Facilitates communication between the cleaner and the mobile device.
* 16x2 LCD: Displays system status, including sensor readings.
* Power Supply: Powers the Pico, motors, and other components.
# Working:
1. System Startup:
* Upon powering on, the Raspberry Pi Pico initializes the system components (sensors, motors, LCD, and Bluetooth).
2. Sensor Data Processing:
* The MQ2 gas sensor continuously monitors for the smell of waste.
* The PIR sensor detects objects or waste in the pond.
3. Displaying Sensor Data:
* The LCD displays real-time data from the sensors, indicating whether the sensors have detected waste.
4. Bluetooth Commands:
* The user connects to the robot via the HC-05 Bluetooth module using a mobile app.
* The following commands are sent for controlling the robot:
  * Movement: Forward, Backward, Left, Right (commands 1-4).
  * Robotic Arm: Up, Down, Grip, Release (commands 5-8).
5. Waste Collection:
* If waste is detected via the PIR sensor, the robotic arm automatically collects it.
* Alternatively, the user can manually control the arm to collect or release waste.
# Algorithm Explanation 
1. Initialize Raspberry Pi Pico and all components.
2. Display "System Starting..." on the LCD.
3. Start an infinite loop:
   * Read values from the MQ2 and PIR sensors.
   * Display "Smell: ON/OFF" based on MQ2 sensor reading.
   * Display "PIR: ON/OFF" based on PIR sensor reading.
   * If a Bluetooth command is received, execute the corresponding movement or arm action.
   * If the MQ2 or PIR sensor detects waste, move to the location and activate the robotic arm to collect it.
4. Repeat the loop continuously.
5. If a shutdown command is received, stop all motors and display "System Shutting Down."
# Project Advantages:
* Automated Cleaning: The system can autonomously detect and collect waste, reducing the need for manual cleaning efforts.
* Wireless Control: The cleaner can be remotely controlled via Bluetooth, allowing flexibility and ease of use.
* Low-Cost Solution: Uses affordable, readily available components like the Raspberry Pi Pico and HC-05 Bluetooth module.
* Environmentally Friendly: Automates the cleaning of ponds, contributing to environmental conservation efforts.
* Customizable: The system can be further enhanced with additional sensors or functionality as needed.
