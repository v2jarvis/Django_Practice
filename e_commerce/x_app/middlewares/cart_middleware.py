# import neccesory modules.
# --------------- Old Code -------------------
# import json


# class CartMiddleware:
#     """
#     Middleware to handle cart operations for anonymous user.
#     """

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         """
#         This method is called for each request.
#         """
#         cart = request.COOKIES.get("cart", "{}")
#         request.cart = json.loads(cart)
#         response = self.get_response(request)
#         response.set_cookie("cart", json.dumps(request.cart), max_age=3600)
#         return response

# # Import necessary modules

import json

class CartMiddleware:

        """

        Middleware to handle cart operations for anonymous users.

        """

        def __init__(self, get_response):
            self.get_response= get_response


        def __call__(self, request):
            cart = request.COOKIES.get("cart", "{}")

            request.cart = json.loads(cart)
            response = self.get_response(request)

            if request.path!= "/logout/":
                if 'cart' in response.cookies:
                    response.set_cookie("cart",
                    response.cookies['cart'].value)
                else:
                    response.set_cookie("cart",
                    json.dumps(request.cart))
            return response

# end of middleware class
