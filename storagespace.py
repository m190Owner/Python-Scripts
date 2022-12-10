import os
import sys

# Get a list of all storage drives on the system
drives = []
if sys.platform == "win32":
    # Windows
    from ctypes import windll
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
else:
    # Other platforms (assume Unix-like)
    for path in os.listdir("/media"):
        drives.append(os.path.join("/media", path))

# Print the available space on each drive
for drive in drives:
    try:
        total, used, free = os.statvfs(drive)
        print("{}: {} GB free".format(drive, free * 1.0 / 1024 / 1024 / 1024))
    except OSError:
        print("{}: Unable to determine available space".format(drive))
