#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if (len(sys.argv) != 4):
    sys.exit("Usage Error: calculadora.py función operando1 operando2.")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        sys.exit("Error: intento de divir entre 0.")


function = sys.argv[1]
try:
    operand1 = float(sys.argv[2])
    operand2 = float(sys.argv[3])
except ValueError:
    sys.exit("Error: los operandos deben ser números")

if (function == "sumar"):
    result = add(operand1, operand2)
    print operand1, "+", operand2, "=", result

elif (function == "restar"):
    result = sub(operand1, operand2)
    print operand1, "-", operand2, "=", result

elif (function == "multiplicar"):
    result = mult(operand1, operand2)
    print operand1, "x", operand2, "=", result

elif (function == "dividir"):
    result = divide(operand1, operand2)
    print operand1, "/", operand2, "=", result

else:
    print "Error: funciones: sumar restar multiplicar dividir."
