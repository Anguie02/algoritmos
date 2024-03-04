from flask import Flask, render_template, request, jsonify
import spacy
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

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

    def entrenar_modelo_recomendacion(self):
        # Lógica para entrenar el modelo de recomendación (simulación)
        X = np.array([[1, 0, 1, 0, 1, 0],  # Compró Herramientas y Sierra
                      [0, 1, 0, 1, 0, 1],   # Compró Fijaciones y Destornillador
                      [1, 1, 0, 1, 0, 0]])  # Compró Herramientas, Fijaciones, Martillo
        y = np.array([1, 2, 0])  # Ejemplo de etiquetas (pueden ser índices de productos)
        self.modelo_recomendacion.fit(X, y)

    def procesar_mensaje(self, mensaje):
        doc = self.nlp(mensaje.lower())
        tokens = [token.text for token in doc]

        # Aquí puedes agregar lógica para interpretar los tokens y generar una respuesta
        respuesta = self.generar_respuesta(tokens)
        self.mensajes.append({"usuario": mensaje, "asistente": respuesta})
        return respuesta

    def generar_respuesta(self, tokens):
        # Lógica para interpretar los tokens y generar una respuesta
        # Por ahora, simplemente recomendar un producto basado en el modelo
        recomendacion = self.recomendar_producto()
        return f"Recomendación: {recomendacion}"

    def recomendar_producto(self):
        historial_compras = [item["producto"] for item in self.carrito]
        caracteristicas_usuario = [1 if producto in historial_compras else 0 for producto in self.productos]
        recomendacion = self.modelo_recomendacion.predict([caracteristicas_usuario])[0]
        return self.productos[recomendacion]

# Crear una instancia del asistente virtual
asistente = AsistenteFerreteria()

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    mensaje_usuario = request.form['mensaje_usuario']
    respuesta_asistente = asistente.procesar_mensaje(mensaje_usuario)
    return jsonify({"respuesta_asistente": respuesta_asistente, "mensajes": asistente.mensajes})

if __name__ == '__main__':
    app.run(debug=True)
