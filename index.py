from flask import Flask, render_template

app=Flask(__name__)

"""
@app.route('/')
def principal():
    return "Bienvenido  a mi sitio web con python"

@app.route('/contacto')
def contacto():
    return "Esta es la pagina de contacto"
"""
@app.route('/')
def principal():
    return render_template('registro.html')

@app.route('/salones')
def mostrarSalones():
    salones=("Salon1", "Salon2", "Salon3", "Salon4", "Salon5", "Salon6")
    return render_template('salones.html', salones=salones)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ =='__main__':
    app.run(debug=True, port=5017)