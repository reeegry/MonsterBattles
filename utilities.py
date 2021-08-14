def transform_class_name(name):
    '''
    Gets "CamelCase" name of class then parse it to "Camel case"
    '''
    return ''.join(' ' + char if char.isupper() else char.strip() for char in name).strip()