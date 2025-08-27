def is_valid_hex_code(s):
    if s[0] != '#' or len(s) != 7:
        return False
    for c in s[1:]:
        if c.upper() not in '0123456789ABCDEF':
            return False
    return True

print(is_valid_hex_code("#CD5C5C"))
print(is_valid_hex_code("#EAECEE"))
print(is_valid_hex_code("#eaecee"))
print(is_valid_hex_code("#CD5C58C"))
print(is_valid_hex_code("#CD5C5Z"))
print(is_valid_hex_code("#CD5C&C"))
print(is_valid_hex_code("CD5C5C"))
