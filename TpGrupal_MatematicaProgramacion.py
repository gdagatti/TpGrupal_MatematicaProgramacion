"""Conversión de Números:
Desarrollar un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos."""
###Integrantes:
#   * Contreras, Agustín -  DNI: 
#   * Cortes, Leonardo - DNI: 34711991
#   * Cuello, Franco - DNI:
#   * Dagatti, German - DNI: 31230293
#   * Demiryi, Nicolás - DNI: 39717139
# ###

# Definición de Funciones 

def decimal_binario(decimal): # Función que convierte un número decimal a binario 
    binario = "" # Se genera una cadena de texto vacía 
    while decimal > 0: 
        residuo = decimal % 2 #Calcula el residuo de la división del número ingresado y 2
        binario = str(residuo) + binario # Va formando el string de 0 y 1 que componen al numero binario final 
        decimal //= 2 # Calcula el cociente exacto entre el número ingresado y 2 
    return validar_binario(binario) # LLama a la función validar_binario. 

def validar_binario(binario):
    if binario:  # Verifica si la cadena 'binario' no está vacía
        return binario
    else:
        return "0"

def binario_decimal(binario):# Función que convierte un número binario a decimal
    decimal = 0
    potencia = len(binario) - 1 # Calcula la potencia más significativa del número binario 
    for digito in binario: # Genera un ciclo que recorre el número decimal y genera la sumatoria de las potencias de 2
        decimal += int(digito) * (2 ** potencia) # Sumatoria de las potencias de 2 por el dígito de esa posición
        potencia -= 1 # Disminuye en uno la potencia 
    return decimal

#Optimización por IA (Copilot)
def main():
    print("Seleccione una opción:")
    print("[D] Convertir de DECIMAL a BINARIO")
    print("[B] Convertir de BINARIO a DECIMAL")

    opcion = input("Ingrese la opción seleccionada: ").strip().upper()

    if opcion == "D":  
        try:
            numero_decimal = int(input("Ingrese su número en base 10: "))
            print(f"Decimal {numero_decimal} a binario: {decimal_binario(numero_decimal)}")
        except ValueError:
            print("Error: Ingrese un número válido.")
    
    elif opcion == "B":
        binario = input("Ingrese su número en base 2: ").strip()
        if all(d in "01" for d in binario):  # Verifica que la entrada sea binaria
            print(f"Binario {binario} a decimal: {binario_decimal(binario)}")
        else:
            print("Error: Ingrese un número binario válido.")

    else:
        print("La opción escogida no es válida.")



# Programa principal
if __name__ == "__main__":
    main()

