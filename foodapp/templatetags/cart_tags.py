from django import template

register = template.Library()

@register.filter
def get_item(cart, item_id):
    """Get item quantity from the session cart."""
    
    return cart.get(str(item_id), 0)

