**Raspberry Pi Project – Blinking LED (Rewritten in UK English)**

Switching an LED on and off is often considered the *“Hello World”* of hardware programming. It introduces the basics of controlling a GPIO output and helps confirm that your wiring is correct. As your projects grow, you will reuse this same approach when working with motors, relays, sensors, and more advanced embedded systems.

### **Hardware Required**

- Raspberry Pi
- Pi T‑Cobbler Plus
- Breadboard
- 2 × Male-to-Male jumper wires
- 1 × LED
- 1 × 220 Ω resistor
- Installed on the Pi: Python 3, Visual Studio Code



## **Hardware Setup**

### **1. Connecting the Ribbon Cable**

The Ribbon Cable includes notches to ensure correct orientation. However, the Raspberry Pi’s GPIO header does **not** have a matching notch, so incorrect alignment may prevent the circuit from working or even damage the Pi.

Your document notes that *“the Ribbon cable must run straight between the two boards with no twist… notches outward from their respective PCBs.”*

- First connect the Ribbon Cable to the T‑Cobbler (notch at the top).
- Then connect the other end to the Raspberry Pi, ensuring the cable runs straight.

Insert the T‑Cobbler into the breadboard carefully to avoid bending the pins.

------

## **2. Wiring the Breadboard**

Prepare:

- 2 × jumper wires
- 1 × LED
- 1 × 220 Ω resistor

Follow these steps:

1. Connect a jumper wire from the **left power rail (+)** to **Row 5**, aligning with **GND** on the T‑Cobbler.
2. Connect the other end of this wire to **Row 5, Column A** on the breadboard.
3. Connect the second jumper wire to **Row 6, Column A**, which corresponds to **GPIO17** on the T‑Cobbler.
4. Connect the other end of this wire to **Row 27, Column A**.
5. Insert the resistor between **Row 27 (+ rail)** and **Row 27, Column B**.
6. Insert the LED:
   - Long leg (positive) → **Column E, Row 26**
   - Short leg (negative) → **Column E, Row 27**

Your document states: *“The longer pin is + and the shorter one is -.”*

------

## **Software Setup**

### **1. Python**

Raspberry Pi OS includes Python 3 by default. Check the version using:

```
python3 --version
```

If Python is missing or outdated, download it from python.org.

### **2. Install Visual Studio Code**

Install VS Code and ensure the Python extension is enabled.

------

## **3. Create the LED Script**

Create a new folder, then a Python file named **led.py**. Add the following code:

```
from gpiozero import LED
from time import sleep

# Initialise an LED connected to GPIO pin 17
led = LED(17)

while True:
    led.on()
    print('LED ON')
    sleep(0.5)

    led.off()
    print('LED OFF')
    sleep(0.5)
```

As your document explains, *“This code creates a simple blinking LED effect by turning the LED on for 0.5 seconds… and repeating the cycle indefinitely.”*

Run the file in VS Code. You will see “LED ON” and “LED OFF” printed in the terminal, and the LED will flash accordingly.