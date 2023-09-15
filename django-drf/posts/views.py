from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view()
def calculator(request):
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operator = request.GET.get('operators')
    
    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    elif operator == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
        
    data = {
        'type' : 'FBV',
        'result' : result,
    }
    
    return Response(data)


class calculatorAPIView(APIView):
    def get(self, request):
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operator = request.GET.get('operators')
        
        if operator == '+':
            result = int(num1) + int(num2)
        elif operator == '-':
            result = int(num1) - int(num2)
        elif operator == '*':
            result = int(num1) * int(num2)
        elif operator == '/':
            result = int(num1) / int(num2)
        else:
            result = 0
            
        data = {
            'type' : 'CBV',
            'result' : result,
        }
            
    def post(self, request):
        data = {
            'type' : 'CBV',
            'method' : 'POST',
            'result' : 0,
        }
        
        return Response(data)