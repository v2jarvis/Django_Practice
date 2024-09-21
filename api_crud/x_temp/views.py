"""
This is the view.py and top of the file import the necessary module.
"""

from django.shortcuts import render


def contact(request):
    """
    This function handles the contact page of the website.
    """
    return render(request, "contact.html")

# def custom_404(request, exception):
#     """
#     This function handles the 404 error page of the website.
#     """
#     return render(request, '404.html', status=404)