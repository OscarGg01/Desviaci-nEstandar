from src.logica.calculos import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular


def main():
    try:
        num_elementos = int(input("¿Cuántos elementos deseas ingresar?: "))

        if num_elementos <= 0:
            print("Debes ingresar un número mayor a 0.")
            return

        elementos = []
        for i in range(num_elementos):
            while True:
                try:
                    elemento = float(input(f"Ingrese el elemento {i + 1}: "))
                    elementos.append(elemento)
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")

        media = calcular_media(elementos)
        desviacion = calcular_desviacion_estandar(elementos)

        print("\nResultado:")
        print(f"Número de elementos: {num_elementos}")
        print(f"Elementos ingresados: {elementos}")
        print(f"Media: {media}")
        print(f"Desviación estándar: {desviacion}")

    except NoSePuedeCalcular as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    main()
