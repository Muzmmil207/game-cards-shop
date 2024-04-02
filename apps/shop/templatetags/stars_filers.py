from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def show_star_rating(rating):
    """Custom tag to generate HTML star ratings based on a rating value."""
    full_stars = int(rating)
    empty_stars = 5 - full_stars
    star_html = ""
    for i in range(full_stars):
        star_html += '<li><i class="fa fa-star-o"></i></li>'
    for i in range(empty_stars):
        star_html += '<li class="no-star"><i class="fa fa-star-o"></i></li>'
    return mark_safe(star_html)
