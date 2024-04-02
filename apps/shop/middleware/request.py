from utils.functional import get_full_url


class RequestMiddleware:
    """
    Access Request Object Inside the Models and Signals.
    Note: I don't know is it good practice to access request object inside the models and signals.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        request.get_full_url = get_full_url(request)

        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)

        return response
