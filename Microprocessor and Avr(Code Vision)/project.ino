// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;

int speedUpSwitch = 2; // Pin for the speed up switch
int speedDownSwitch = 3; // Pin for the speed down switch

int speed = 128; // Initial speed value (between 0 and 255)
int maxSpeed = 255; // Maximum speed value

void setup() {
    // Set all the motor control pins to outputs
    pinMode(enA, OUTPUT);
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);

    // Set up the speed control switches
    pinMode(speedUpSwitch, INPUT_PULLUP);
    pinMode(speedDownSwitch, INPUT_PULLUP);

    // Turn on motor A
    analogWrite(enA, speed);
    // Set the direction of motor A
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
}

void loop() {
    speedControl();
}

// This function lets you control speed of the motor
void speedControl() {
    // Check if the speed up switch is pressed
    if (digitalRead(speedUpSwitch) == LOW && speed < maxSpeed) {
        speed += 5;
    }

    // Check if the speed down switch is pressed
    if (digitalRead(speedDownSwitch) == LOW) {
        if (speed > 0) {
            speed -= 5;
        } else {
            // Set speed to the maximum value when reaching zero
            speed = maxSpeed;
        }
    }

    // Update the speed of motor A
    analogWrite(enA, speed);
}
