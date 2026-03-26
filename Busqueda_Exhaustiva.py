import matplotlib.pyplot as plt
import math
import tkinter as tk
import numpy as np
import re

class BusquedaExhaustiva:

    def calcular_minimo(self, funcion, a, b, precision):
        x_minimo = a
        fx_minimo = funcion(a)

        for x in np.arange(a, b + precision, precision):
            fx = funcion(x)
            if fx < fx_minimo:
                fx_minimo = fx
                x_minimo = x

        return x_minimo, fx_minimo

    def convertir_texto_funcion(self, expresion):
        funcion = lambda x: eval(expresion, {"x": x, "sen": math.sin,"sin": math.sin,"cos": math.cos, "pi": math.pi})
        return funcion

    def limpiar_expresion(self, expresion):
        expresion = expresion.replace('²', '**2')
        expresion = expresion.replace('³', '**3')
        expresion = expresion.replace('⁴', '**4')
        expresion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expresion)
        
        return expresion

    def al_presionar_calcular(self, entrada_funcion, entrada_a, entrada_b, entrada_precision, etiqueta_resultado, ventana):
        
        try:
            expresion = self.limpiar_expresion(entrada_funcion.get())
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            precision = float(entrada_precision.get())

            funcion = self.convertir_texto_funcion(expresion)

            etiqueta_resultado.config(text="Calculando...")
            ventana.update()

            x_min, fx_min = self.calcular_minimo(funcion, a, b, precision)

            etiqueta_resultado.config(
                text=f"x óptimo = {x_min:.4f}\n   f(x) = {fx_min:.4f}"
            )

        except Exception as e:
            etiqueta_resultado.config(text=f"Error: {str(e)}")

    def crear_interfaz(self):
        ventana = tk.Tk()
        ventana.title("Optimización por Búsqueda Exhaustiva")
        ventana.geometry("380x340")
        ventana.resizable(False, False)

        tk.Label(ventana, text="Ingresa la función f(x):").pack(pady=(15, 2))
        entrada_funcion = tk.Entry(ventana, width=35)
        entrada_funcion.pack()

        tk.Label(ventana, text="ingresa el limite inferior:").pack(pady=(10, 2))
        entrada_a = tk.Entry(ventana, width=15)
        entrada_a.pack()

        tk.Label(ventana, text="ingresa el limite superior:").pack(pady=(5, 2))
        entrada_b = tk.Entry(ventana, width=15)
        entrada_b.pack()

        tk.Label(ventana, text="Precisión esperada del modelo:").pack(pady=(5, 2))
        entrada_precision = tk.Entry(ventana, width=15)
        entrada_precision.pack()

        etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"), fg="#333")

        tk.Button(
            ventana,
            text="Calcular Mínimo",
            command=lambda: self.al_presionar_calcular(
                entrada_funcion, entrada_a, entrada_b, entrada_precision, etiqueta_resultado, ventana
            ),
            bg="#EE37D8", fg="white", padx=10, pady=5
        ).pack(pady=15)

        etiqueta_resultado.pack()
        ventana.mainloop()


optimizador = BusquedaExhaustiva()
optimizador.crear_interfaz()