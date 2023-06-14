from django import template
from resume.models import *

register = template.Library()

@register.inclusion_tag('resume/stars.html')
def difficulty(diff):
    return {'range': range(5),
            'difficulty': diff}