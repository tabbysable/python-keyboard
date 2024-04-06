import storage, usb_cdc, usb_midi, usb_hid
import board, digitalio

# Configuration Options

# Key to hold down to show the CIRCUITPY drive
# key D is index 31, R4 C8
ROW=board.R4
COL=board.C8

# Uncomment if you need a Boot Keyboard
# This is needed for some BIOSes, KVMs, and old Macs
# Boot Keyboard does not allow mouse or consumer control features
# bootKeyboard = True

REFERENCE_BOOT_KEYBOARD_DESCRIPTOR=bytes((
0x05, 0x01,        # Usage Page (Generic Desktop Ctrls)
0x09, 0x06,        # Usage (Keyboard)
0xA1, 0x01,        # Collection (Application)
0x05, 0x07,        #   Usage Page (Kbrd/Keypad)
0x19, 0xE0,        #   Usage Minimum (0xE0)
0x29, 0xE7,        #   Usage Maximum (0xE7)
0x15, 0x00,        #   Logical Minimum (0)
0x25, 0x01,        #   Logical Maximum (1)
0x75, 0x01,        #   Report Size (1)
0x95, 0x08,        #   Report Count (8)
0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Pr
0x95, 0x01,        #   Report Count (1)
0x75, 0x08,        #   Report Size (8)
0x81, 0x01,        #   Input (Const,Array,Abs,No Wrap,Linear
0x95, 0x03,        #   Report Count (3)
0x75, 0x01,        #   Report Size (1)
0x05, 0x08,        #   Usage Page (LEDs)
0x19, 0x01,        #   Usage Minimum (Num Lock)
0x29, 0x05,        #   Usage Maximum (Kana)
0x91, 0x02,        #   Output (Data,Var,Abs,No Wrap,Linear,P
0x95, 0x01,        #   Report Count (1)
0x75, 0x05,        #   Report Size (5)
0x91, 0x01,        #   Output (Const,Array,Abs,No Wrap,Linea
0x95, 0x06,        #   Report Count (6)
0x75, 0x08,        #   Report Size (8)
0x15, 0x00,        #   Logical Minimum (0)
0x26, 0xFF, 0x00,  #   Logical Maximum (255)
0x05, 0x07,        #   Usage Page (Kbrd/Keypad)
0x19, 0x00,        #   Usage Minimum (0x00)
0x2A, 0xFF, 0x00,  #   Usage Maximum (0xFF)
0x81, 0x00,        #   Input (Data,Array,Abs,No Wrap,Linear,
0xC0,              # End Collection
))

reference_keyboard = usb_hid.Device(
    report_descriptor=REFERENCE_BOOT_KEYBOARD_DESCRIPTOR,
    usage=0x06,
    usage_page=0x01,
    report_ids=(0,),
    in_report_lengths=(8,),
    out_report_lengths=(1,),
    )

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

# Hide the USB MIDI interfaces so we're a pure HID
usb_midi.disable()

# Hide the configuration interfaces and let circuitpy write
if not show_config:
    storage.remount("/",readonly=False)
    storage.disable_usb_drive()
    usb_cdc.disable()
    if bootKeyboard:
        usb_hid.enable((reference_keyboard,), boot_device=1)
