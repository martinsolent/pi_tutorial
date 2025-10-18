import time
from LCD import LCD

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x3f, True)  # Using Raspberry Pi revision 2 and above, I2C address 0x3f, backlight enabled

# Display messages on the LCD
lcd.message("LCD TESTER", 1)   # Display 'Add Text' on line 1
lcd.message("Hello", 2)        # Display 'Add Text' on line 2

# Keep the messages displayed for 5 seconds
time.sleep(30)

# Clear the LCD display
lcd.clear()