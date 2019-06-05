

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at Leads API.")


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def get_sum(request):
    """
    Get Result for Sum
    """
    data = {}
    number1 = int(request.data.get('number1', 0))
    number2 = int(request.data.get('number2', 0))
    data['sum'] = number1 + number2
    return Response(data, status=status.HTTP_200_OK)
