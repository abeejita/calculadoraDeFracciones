from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fractions import Fraction
from json import loads, dumps

# Creación de views
def index(request):
    return render(request, "index.html")

# Función que suma dos fracciones.
@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    resultado = Fraction(body['numerador1'], body['denominador1']) + Fraction(body['numerador2'], body['denominador2'])
    dic_resultado = {"num":resultado.numerator, "den":resultado.denominator}
    json_resultado = dumps(dic_resultado)
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")

# Función que resta dos fracciones.
@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    resultado = Fraction(body['numerador1'], body['denominador1']) - Fraction(body['numerador2'], body['denominador2'])
    dic_resultado = {"num":resultado.numerator, "den":resultado.denominator}
    json_resultado = dumps(dic_resultado)
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")

# Función que multiplica dos fracciones.
@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    resultado = Fraction(body['numerador1'], body['denominador1']) * Fraction(body['numerador2'], body['denominador2'])
    dic_resultado = {"num":resultado.numerator, "den":resultado.denominator}
    json_resultado = dumps(dic_resultado)
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")

# Función que divide dos fracciones.
@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    resultado = Fraction(body['numerador1'], body['denominador1']) / Fraction(body['numerador2'], body['denominador2'])
    dic_resultado = {"num":resultado.numerator, "den":resultado.denominator}
    json_resultado = dumps(dic_resultado)
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")
