class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.number_requests = 0
        self.number_of_exceptions = 0
        self.context_response = {
            "message": {
                "warning": "There is no more ink in the printer"
            }
        }

    def __call__(self, request):
        self.number_requests += 1
        print(f"The number of requests => {self.number_requests}")
        response = self.get_response(request)
        return response

    # CALLED BEFORE REQUESTS:
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print(f"view name is {view_func.__name__}")
        print(view_args)
        print(request.path)
        print(request.headers['Accept-Language'])
        print(request.headers['Host'])
        print(request.META['REQUEST_METHOD'])
        print(request.COOKIES)
        print(request.body)
        print(request.META['HTTP_USER_AGENT'])

    def process_exception(self, request, exception):
        self.number_of_exceptions += 1
        print(
            f"The total number of exceptions is => {self.number_of_exceptions}")
        pass

    # CALLED BEFORE A RESPONSE IS SENT:
    def process_template_response(self, request, response):
        response.context_data["new_data"] = self.context_response
        return response


"""_summary_
Three optional methods that execute at different points of the view request/ response life cycle

CALLED DURING REQUEST:
process_request(request)
process_view(request, view_func,*view_args, **view_kwargs) => happens before the request gets to the view

CALLED DURING RESPONSE:
process_exception(request,exception)
        only if the view raised an expection

process_template_response(request,response)

if you use process_template_response make sure the view returns the template like this  =>   return TemplateResponse(request, 'home.html', context)


process_response(request,response)
"""
