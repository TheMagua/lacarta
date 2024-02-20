from django.core.exceptions import ValidationError
import re


def validate_digits(value):
    if not value.isdigit():
        raise ValidationError("This field only accepts digits.")
    
def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError("This field only accepts letters.")

def validate_alnum(value):
    if not value.isalnum():
        raise ValidationError("This field only accepts letters y digits.")


def validate_letters_and_spaces(value):
    if not re.match(r'^[A-Za-z\sáéíóúÁÉÍÓÚ]*$', value):
        raise ValidationError(
            f'{value} contains illegal characters. Only letters and white spaces are allowed.'
        )
        
def validate_letters_numbers_and_spaces(value):
    if not re.match(r'^[A-Za-z0-9\sáéíóúÁÉÍÓÚ]*$', value):
        raise ValidationError(
            f'Contains illegal characters. Only letters, numbers and blank spaces are allowed.'
        )