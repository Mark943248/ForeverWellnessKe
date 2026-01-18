import bleach
from django import template
from bleach.css_sanitizer import CSSSanitizer
from django.utils.safestring import mark_safe

register = template.Library()

# 1. Define allowed HTML tags
# CKEditor 5 generates these common tags. Adjust based on your toolbar configuration.
ALLOWED_TAGS = [
    'p', 'div', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'strong', 'b', 'em', 'i', 'u', 'strike', 's', 'del',
    'ul', 'ol', 'li', 'blockquote', 'code', 'pre',
    'a', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
    'span', 'sub', 'sup'
]

# 2. Define allowed attributes
# This is a dictionary where keys are tag names and values are lists of allowed attributes.
ALLOWED_ATTRIBUTES = {
    '*': ['class', 'style'],  # Allow 'class' and 'style' on all tags (common in CKEditor)
    'a': ['href', 'title', 'target', 'rel'],
    'img': ['src', 'alt', 'width', 'height', 'title'],
    'table': ['border', 'cellpadding', 'cellspacing', 'align'],
}

# 3. Define allowed CSS styles (if you allow the 'style' attribute above)
# CKEditor uses inline styles for text alignment, image resizing, etc.
ALLOWED_STYLES = [
    'color', 'background-color', 'font-size', 'font-family',
    'text-align', 'width', 'height', 'float', 'margin', 'padding',
    'border', 'list-style-type'
]

# 4. Define allowed protocols for links
ALLOWED_PROTOCOLS = ['http', 'https', 'mailto', 'tel']

css_sanitizer = CSSSanitizer(allowed_css_properties=ALLOWED_STYLES)

@register.filter(name='sanitize_html')
def sanitize_html(value):
    """
    Sanitizes HTML content using Bleach to prevent XSS attacks.
    Allowed tags, attributes, and styles are configured above.
    """
    if not value:
        return ""

    cleaned_value = bleach.clean(
        value,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        css_sanitizer=css_sanitizer,
        protocols=ALLOWED_PROTOCOLS,
        strip=True  # True = strip disallowed tags; False = escape them
    )

    # We mark the result as safe so Django renders the HTML
    return mark_safe(cleaned_value)