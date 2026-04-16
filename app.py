from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave-por-defecto')

@app.route('/')
def home():
    return """
    <h1>¡Bienvenido a Tienda Gamer!</h1>
    <p>Servidor corriendo en Ubuntu Server 25 con VirtualBox</p>
    <p><strong>Parte 2 - Configuración de herramientas completada</strong></p>
    """

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
