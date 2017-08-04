from django import template

import random
import markdown2
import string

from minerals.models import Mineral


register = template.Library()


@register.inclusion_tag('minerals/logo_header.html')
def logo_header():
    """Displays the logo and header for the website"""
    return {}


@register.inclusion_tag('minerals/random_mineral.html')
def random_mineral():
    return {"mineral": random.choice(Mineral.objects.all())}


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML"""
    html_body = markdown2.markdown(markdown_text)
    return html_body


@register.inclusion_tag('minerals/alpha_nav.html')
def alpha_nav(current):
    alpha_list = [x for x in string.ascii_uppercase]
    return {'alpha_list': alpha_list, 'current': current}


@register.inclusion_tag('minerals/group_nav.html')
def group_search(current):
    groups = [
                'silicates',
                'oxides',
                'sulfates',
                'sulfides',
                'carbonates',
                'halides',
                'sulfosalts',
                'phosphates',
                'borates',
                'organic',
                'arsenates',
                'native',
                'other']

    return {'groups': groups, 'current': current}



