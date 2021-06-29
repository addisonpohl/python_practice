#!/usr/bin/env python3

import shutil
import psutil

# This script is used to practice with operating with the OS.

def check_disk_usage(disk):
    """Returns true if the disk usuage is more than 20% free"""

    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """Checks usuage for 1 second and determines healthy if less than 75%"""

    useage = psutil.cpu_percent(1)
    return useage < 75


if not check_disk_usage("/") or not check_cpu_usage:
    print("A check up is needed")
else:
    print("Everything looks good!")
