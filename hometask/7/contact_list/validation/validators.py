from pyisemail import is_email
from phonenumbers import parse, is_valid_number, NumberParseException


def valid_email(email: str) -> bool:
    return is_email(email)


def valid_phone_number(number: str) -> bool:
    try:
        parsed = parse(number)
    except NumberParseException:
        return False

    return is_valid_number(parsed)


def valid_name(name: str) -> bool:
    if len(name) < 3:
        raise ValueError('Name can not be shorter than than 3 characters')

    for substring in name.split():
        if not substring.isalpha():
            raise ValueError('Name can only contain alpha characters')

    return True
