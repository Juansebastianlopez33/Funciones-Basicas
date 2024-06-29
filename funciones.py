#*****
#Sena Mosquera Cba
#Ficha: 2877795
#Aprendiz: Juan Sebastian Lopez
#Version: 2.0
#Fecha: 12/03/2024
#******
#importamos random para poder generar numeros aleatorios
import random
from colorama import Fore , Back
from Modules.final import main as selecion_final
from os import system as osystem
#definimos 2 variables que almcenen los numeros aleatorios
def main():
    while True:
        osystem('cls')
        num1 = random.randint(1, 20)
        num2 = random.randint(1,20)
        #imprimimos un saludo de bienvenida
        print(Fore.LIGHTMAGENTA_EX, Back.WHITE)
        print("\n"+"bienvenido a operaciones basicas sus numeros generados son:"+"\n",num1," y ", num2)
        #usando print le decimos  el usuario que operacion se esta generando 
        #realizamos la operacion llamando las variables y usamos los operadores logicos
        suma = print("\n"+"la suma de sus numeros generados son:"+"\n",num1 + num2)
        resta = print("\n"+"la resta de sus numeros generados son:"+"\n", num1 - num2)
        divicion = print("\n"+"la divicion de sus numeros generados son:"+"\n", num1 / num2)
        divicion_entera = print("\n"+"la divicion entera de sus numeros generados son:"+"\n", num1 // num2)
        residuo = print("el residuo de dividir sus numeros generados es:"+"\n",num1 % num2)
        multiplicacion = print("la multiplicacion de sus numeros generados es:"+"\n",num1 * num2)
        print(Fore.RESET, Back.RESET)
        verifi = selecion_final()
        if verifi == 'N':
            osystem('cls')
            break
if __name__ == '__main__':
    main()
