from django.shortcuts import render
from django.views import View


class OpenApiView(View):
    """
    View for displaying API documentation
    """

    template = 'openapi.html'

    def get(self, request):

        return render(request, self.template)
