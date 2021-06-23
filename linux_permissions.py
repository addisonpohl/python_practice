def octal_to_string(octal):
    """Tranlates numeric linux permissions"""

    perms = {
            "0": ('---'),
            "1": ('--x'),
            "2": ('-w-'),
            "3": ('-wx'),
            "4": ('r--'),
            "5": ('r-x'),
            "6": ('rw-'),
            "7": ('rwx')
            }
    result = ""

    for num in str(octal):
        result += perms[num]

    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------
