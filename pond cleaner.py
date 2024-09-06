import time
# Mock classes for Pin and UART to simulate microcontroller behavior
class Pin:
    IN = 0
    OUT = 1
    
    def __init__(self, pin, mode):
        self.pin = pin
        self.mode = mode
        self.state = 0  # Simulate pin state
        
    def value(self, val=None):
        if val is None:
            return self.state
        self.state = val

    def on(self):
        self.state = 1
        print(f"Pin {self.pin} ON")

    def off(self):
        self.state = 0
        print(f"Pin {self.pin} OFF")


class UART:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.buffer = []

    def any(self):
        return len(self.buffer) > 0

    def read(self, n):
        if self.buffer:
            return self.buffer.pop(0)
        return None

    def write(self, data):
        print(f"UART{self.port}: {data}")

# Setup components
lcd_rs = Pin(0, Pin.OUT)
lcd_en = Pin(1, Pin.OUT)
lcd_d4 = Pin(2, Pin.OUT)
lcd_d5 = Pin(3, Pin.OUT)
lcd_d6 = Pin(4, Pin.OUT)
lcd_d7 = Pin(5, Pin.OUT)

pir_sensor = Pin(6, Pin.IN)
mq2_sensor = Pin(7, Pin.IN)

motor_left = Pin(8, Pin.OUT)
motor_right = Pin(9, Pin.OUT)
motor_forward = Pin(10, Pin.OUT)
motor_backward = Pin(11, Pin.OUT)

arm_up = Pin(12, Pin.OUT)
arm_down = Pin(13, Pin.OUT)
arm_grip = Pin(14, Pin.OUT)
arm_release = Pin(15, Pin.OUT)

bluetooth = UART(0, 9600)

# LCD Functions (Simulated)
def lcd_command(cmd):
    print(f"LCD Command: {cmd}")
    lcd_rs.value(0)
    lcd_d4.value((cmd >> 4) & 1)
    lcd_d5.value((cmd >> 3) & 1)
    lcd_d6.value((cmd >> 2) & 1)
    lcd_d7.value((cmd >> 1) & 1)
    lcd_en.on()
    time.sleep(0.001)
    lcd_en.off()

def lcd_clear():
    lcd_command(0x01)
    time.sleep(0.002)

def lcd_init():
    lcd_command(0x33)
    lcd_command(0x32)
    lcd_command(0x28)
    lcd_command(0x0C)
    lcd_command(0x06)
    lcd_clear()

def lcd_message(message):
    lcd_clear()
    print(f"LCD Message: {message}")
    for char in message:
        lcd_rs.value(1)
        lcd_d4.value((ord(char) >> 4) & 1)
        lcd_d5.value((ord(char) >> 3) & 1)
        lcd_d6.value((ord(char) >> 2) & 1)
        lcd_d7.value((ord(char) >> 1) & 1)
        lcd_en.on()
        time.sleep(0.001)
        lcd_en.off()

# Robot movement
def move_robot(command):
    if command == '1':  # Forward
        motor_forward.on()
        time.sleep(1)
        motor_forward.off()
    elif command == '2':  # Backward
        motor_backward.on()
        time.sleep(1)
        motor_backward.off()
    elif command == '3':  # Left
        motor_left.on()
        time.sleep(1)
        motor_left.off()
    elif command == '4':  # Right
        motor_right.on()
        time.sleep(1)
        motor_right.off()

# Robotic arm control
def control_arm(command):
    if command == '5':  # Arm up
        arm_up.on()
        time.sleep(1)
        arm_up.off()
    elif command == '6':  # Arm down
        arm_down.on()
        time.sleep(1)
        arm_down.off()
    elif command == '7':  # Grip
        arm_grip.on()
        time.sleep(1)
        arm_grip.off()
    elif command == '8':  # Release
        arm_release.on()
        time.sleep(1)
        arm_release.off()

# Main process loop
def main():
    lcd_init()
    try:
        while True:
            # Read sensors (simulated)
            smell_detected = mq2_sensor.value()
            pir_detected = pir_sensor.value()

            # Display sensor statuses on LCD
            if smell_detected:
                lcd_message("Smell: ON")
            else:
                lcd_message("Smell: OFF")

            if pir_detected:
                lcd_message("PIR: ON")
            else:
                lcd_message("PIR: OFF")
            
            # Simulating Bluetooth commands input
            if bluetooth.any():
                command = bluetooth.read(1)
                if command:
                    command = command.decode('utf-8')
                    print(f"Command received: {command}")
                
                    if command in ['1', '2', '3', '4']:  # Movement commands
                        move_robot(command)
                    elif command in ['5', '6', '7', '8']:  # Arm commands
                        control_arm(command)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Program stopped by user.")

# Simulate receiving Bluetooth commands
def simulate_bluetooth_commands():
    commands = ['1', '3', '5', '7', '2', '4', '6', '8']
    for cmd in commands:
        bluetooth.buffer.append(cmd.encode('utf-8'))

if __name__ == "__main__":
    simulate_bluetooth_commands()
    main()
