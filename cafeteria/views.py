from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def landing(request):
    """Public landing page – visible to everyone."""
    return render(request, 'cafeteria/landing.html')


@login_required
def secret_menu(request):
    """
    Secret Lunch Menu – restricted to logged-in users only.
    The @login_required decorator automatically redirects any
    unauthenticated visitor to the login page (LOGIN_URL in settings.py).
    """
    menu_items = [
        {
            'name': 'Roasted Gorax Ribs',
            'description': 'Slow-roasted over an open Endor fire pit, slathered in sweet Sunberry glaze.',
            'emoji': '🍖',
        },
        {
            'name': 'Endorian Sunberry Salad',
            'description': 'Fresh forest greens tossed with golden Sunberries and a tangy bark-vinegar dressing.',
            'emoji': '🍓',
        },
        {
            'name': 'Grilled Yuzzum Skewers',
            'description': 'Tender Yuzzum chunks marinated in spiced tree-sap and grilled to perfection.',
            'emoji': '🍢',
        },
        {
            'name': 'Bantha Milk Stew',
            'description': 'A hearty stew made with creamy Bantha milk, root vegetables, and wild mushrooms.',
            'emoji': '🍲',
        },
        {
            'name': 'Logray\'s Honeycomb Cookies',
            'description': 'Crispy cookies baked with wild honey and Ewok-sacred spices. A tribal favorite!',
            'emoji': '🍪',
        },
    ]
    return render(request, 'cafeteria/secret_menu.html', {'menu_items': menu_items})
