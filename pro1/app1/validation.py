from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

"""
Name Validation
"""
def validate_name(name):
    error_message="Enter the valid username"
    regex=r'^[A-Za-z]*$'
    good_name=re.match(regex,name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message,params={'name':name})



""" 
Age Validation 
"""

# def validate_age(age):
#     if age > 0 and age <100 :
#         raise ValidationError(
#             _("%(value)s is not an even number"),
#             params={"value": age},
#         )