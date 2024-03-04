import spacy
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class AsistenteFerreteria:
    def __init__(self):
        self.carrito = []
        self.historial_pedidos = []
        self.productos = ["Martillo", "Destornillador", "Sierra", "Clavos", "Tornillos", "Fierros"]
        self.categorias = ["Herramientas", "Fijaciones"]
        self.modelo_recomendacion = DecisionTreeClassifier()
        self.entrenar_modelo_recomendacion()

        # Cargar el modelo de spaCy para procesamiento de lenguaje natural
        self.nlp = spacy.load("es_core_news_sm")

        # Mensaje de bienvenida
        print("¡Bienvenido a Ferretería El Tornillo Feliz! ¿En qué puedo ayudarte hoy?")

    def entrenar_modelo_recomendacion(self):
        # Lógica para entrenar el modelo de recomendación (simulación)
        X = np.array([[1, 0, 1, 0, 1, 0],  # Compró Herramientas y Sierra
                      [0, 1, 0, 1, 0, 1],  # Compró Fijaciones y Destornillador
                      [1, 1, 0, 1, 0, 0]])  # Compró Herramientas, Fijaciones, Martillo
        y = np.array([1, 2, 0])  # Ejemplo de etiquetas (pueden ser índices de productos)
        self.modelo_recomendacion.fit(X, y)

    def procesar_mensaje_natural(self, mensaje):
        doc = self.nlp(mensaje.lower())
        tokens = [token.text for token in doc]
        return tokens

    def agregar_al_carrito(self, producto, cantidad):
        self.carrito.append({"producto": producto, "cantidad": cantidad})
        return f"Se ha agregado {cantidad} unidades de {producto} al carrito."

    def recomendar_producto(self):
        historial_compras = [item["producto"] for item in self.carrito]
        caracteristicas_usuario = [1 if producto in historial_compras else 0 for producto in self.productos]
        recomendacion = self.modelo_recomendacion.predict([caracteristicas_usuario])[0]
        return self.productos[recomendacion]

    def registrar_pedido(self):
        if self.carrito:
            self.historial_pedidos.append(list(self.carrito))
            self.carrito = []
            return "Pedido registrado con éxito."
        else:
            return "El carrito está vacío. Agrega productos antes de registrar un pedido."

    def seguimiento_pedidos(self):
        return self.historial_pedidos

# Crear una instancia del asistente virtual
asistente = AsistenteFerreteria()

# Simular historial de compras
historial_compras_simulado = ["Martillo", "Tornillos", "Sierra"]
for compra in historial_compras_simulado:
    asistente.agregar_al_carrito(compra, 1)

# Realizar pedido y obtener recomendación
respuesta_pedido = asistente.registrar_pedido()
recomendacion = asistente.recomendar_producto()

# Mostrar resultados
print(f"Resultado del pedido: {respuesta_pedido}")
print(f"Recomendación de producto: {recomendacion}")
print(f"Seguimiento de pedidos: {asistente.seguimiento_pedidos()}")
