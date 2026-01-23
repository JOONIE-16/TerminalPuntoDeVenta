def calculadora_precios_inteligente():
    while True:
        print("--- CALCULADORA DE PRECIOS INTELIGENTE ---")

        # 2. Entrada de cantidad con validación
        while True:
            try:
                cantidad = int(input("¿Cuántos productos va a ingresar? "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser mayor que 0.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

        # 3. Captura de datos de los productos
        nombres = []
        precios = []
        for i in range(cantidad):
            nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
            
            while True:
                try:
                    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
                    if precio > 0:
                        break
                    else:
                        print("El precio debe ser mayor que 0. Intente de nuevo.")
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")
            
            nombres.append(nombre)
            precios.append(precio)

        # 4. Cálculo del subtotal
        subtotal = sum(precios)

        # 5. Aplicación de lógica de negocio (descuentos y avisos)
        descuento = 0
        if subtotal > 500:
            descuento = subtotal * 0.10
            print("Se ha aplicado un descuento del 10%.")
        elif subtotal < 100:
            print("Advertencia: no se alcanzó el monto mínimo de compra ($100).")

        total = subtotal - descuento

        # 6. Salida de resultados
        print("\nResumen de la compra:")
        for i in range(cantidad):
            print(f"{i + 1}. {nombres[i]} - ${precios[i]:.2f}")
        
        print("--------------------------")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento: ${descuento:.2f}")
        print(f"Total a pagar: ${total:.2f}")
        print("--------------------------")

        # 7. Control de repetición del algoritmo
        volver_inicio = input("¿Desea realizar otra compra? (s/n): ").lower()
        if volver_inicio != 's':
            break

    print("Gracias por usar la calculadora. ¡Hasta pronto!")

if __name__ == "__main__":
    calculadora_precios_inteligente()
