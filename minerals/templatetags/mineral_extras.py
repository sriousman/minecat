from django import template

import random
import markdown2

from minerals.models import Mineral


register = template.Library()


@register.inclusion_tag('minerals/logo_header.html')
def logo_header():
    """Displays the logo and header for the website"""
    return {}


@register.inclusion_tag('minerals/random_mineral.html')
def random_mineral():
    return { "mineral": random.choice(Mineral.objects.all())}


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML"""
    html_body = markdown2.markdown(markdown_text)
    return html_body
