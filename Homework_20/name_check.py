import re



def is_valid_name(name):
    if not (2 <= len(name) <= 50):
        return False

    if not re.match("^[A-Za-zА-Яа-яЁё\s\-]+$", name):
        return False
    
    return True