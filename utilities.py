from screeninfo import get_monitors

screen_property = get_monitors()[0]


def get_resolution():
    return screen_property.height, screen_property.width


def transform_class_name(name):
    '''
    Gets "CamelCase" name of class then parse it to "Camel Case"
    '''
    return ''.join(' ' + char if char.isupper() else char.strip() for char in name).strip()