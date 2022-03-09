def is_isogram(string):
    return string == '' or len(string) == len(set(string.lower()))
