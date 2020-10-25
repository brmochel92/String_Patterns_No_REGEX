def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print ('217-555-8888 is a phone number: ')
print(isPhoneNumber('217-555-8888'))
print('XXX-XXX-XXXX is a phone number:')
print(isPhoneNumber('xxx-xxx-xxxx'))