import storage, usb_cdc
import board, digitalio

# key D is index 31, R4 C8
ROW=board.R4
COL=board.C8

#ROW2COL as used in model/, indicating direction of diodes
ROW2COL = False
pressed = bool(ROW2COL)

show_config = False

# Set up the pins
row = digitalio.DigitalInOut(ROW)
row.direction = digitalio.Direction.OUTPUT
row.drive_mode = digitalio.DriveMode.PUSH_PULL
col = digitalio.DigitalInOut(COL)
col.direction = digitalio.Direction.INPUT
col.pull = digitalio.Pull.DOWN if ROW2COL else digitalio.Pull.UP

# Scan the key
row.value = pressed
if col.value == pressed:
	show_config = True
row.value = not pressed

# Hide the configuration interfaces
if not show_config:
    storage.disable_usb_drive()
    usb_cdc.disable()
