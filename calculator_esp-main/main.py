# Importar
from flask import Flask, render_template, url_for

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')

# La segunda página
@app.route('/<int:size>')
def lights(size):
    return render_template('lights.html', size=size)

# La tercera página
@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Cálculo final
@app.route('/<int:size>/<int:lights>/<int:device>/')
def end(size, lights, device):
    print(f"Debug - size: {size}, lights: {lights}, device: {device}")  # Depuración
    return render_template('end.html', result=result_calculate(size, lights, device))

if __name__ == '__main__':
    app.run(debug=True)
