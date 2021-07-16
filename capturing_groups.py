import re

name1 = "Alfred, John"
name2 = "Adams, Sam"

def rearrange_name(name):
    """Rearranges a first and last name when searching with regex via capture groups"""
    result = re.search(r"^(\w*), (\w*)$", name)
    print(result.groups())
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

print(rearrange_name(name2))
