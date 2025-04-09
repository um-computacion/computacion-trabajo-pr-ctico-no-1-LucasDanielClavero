def decimal_to_roman(num):
    if num < 1 or num > 3999:
        return "Numero fuera de rango (debe estar entre 1 y 3999)"
    
    result = ""
    
    while num >= 1000: #es un poco tosco pero basicamente de apoco va reduciendo el numero que le ingresamos en valores predeterminados y agrega esos mismos valores a su version en Romano
        result += "M"
        num -= 1000
    while num >= 900:
        result += "CM"
        num -= 900
    while num >= 500:
        result += "D"
        num -= 500
    while num >= 400:
        result += "CD"
        num -= 400
    while num >= 100:
        result += "C"
        num -= 100
    while num >= 90:
        result += "XC"
        num -= 90
    while num >= 50:
        result += "L"
        num -= 50
    while num >= 40:
        result += "XL"
        num -= 40
    while num >= 10:
        result += "X"
        num -= 10
    while num >= 9:
        result += "IX"
        num -= 9
    while num >= 5:
        result += "V"
        num -= 5
    while num >= 4:
        result += "IV"
        num -= 4
    while num >= 1:
        result += "I"
        num -= 1     #al final el valor ingresado termina siendo 0 y su contra parte en romano esta completa

    return result