
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class AsistenteVirtual:
    def __init__(self):
        self.carrito = []
        self.pedidos = []
        self.modelo_recomendacion = DecisionTreeClassifier()

    def iniciar_conversacion(self):
        print("¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
        while True:
            mensaje = input("Usuario: ")
            respuesta = self.procesar_mensaje(mensaje)
            print("Asistente: " + respuesta)

    def procesar_mensaje(self, mensaje):
        if "registro" in mensaje.lower():
            return self.registrar_pedido()
        elif "recomendacion" in mensaje.lower():
            return self.recomendar_producto()
        elif "seguimiento" in mensaje.lower():
            return self.seguimiento_pedidos()
        else:
            return "Lo siento, no entiendo. ¿Puedes ser más específico?"

    def registrar_pedido(self):
        producto = input("¿Qué producto deseas agregar al carrito? ")
        cantidad = int(input("¿Cuántos deseas? "))
        self.carrito.append({"producto": producto, "cantidad": cantidad})
        return f"Se ha agregado {cantidad} unidades de {producto} al carrito."

    def entrenar_modelo_recomendacion(self):
        # Lógica para entrenar el modelo de recomendación (simulación)
        X = np.array([[0], [1], [2]])  # Ejemplo de características (pueden ser más complejas)
        y = np.array([0, 1, 2])  # Ejemplo de etiquetas (pueden ser categorías de productos)
        self.modelo_recomendacion = DecisionTreeClassifier()
        self.modelo_recomendacion.fit(X, y)

    def recomendar_producto(self):
        # Lógica para recomendar un producto utilizando el modelo de decisiones
        if not hasattr(self, 'modelo_recomendacion'):
            self.entrenar_modelo_recomendacion()

        # Simulación de entrada de características del usuario para la recomendación
        caracteristicas_usuario = np.array([[1]])
        recomendacion = self.modelo_recomendacion.predict(caracteristicas_usuario)[0]
        return f"Te recomiendo el producto {recomendacion}. ¿Te gustaría agregarlo al carrito?"

    def seguimiento_pedidos(self):
        if not self.pedidos:
            return "No tienes pedidos registrados aún."
        else:
            return f"Tienes {len(self.pedidos)} pedidos. El último pedido es: {self.pedidos[-1]}."

if __name__ == "__main__":
    asistente = AsistenteVirtual()
    asistente.iniciar_conversacion()
