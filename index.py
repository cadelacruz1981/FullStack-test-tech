from flask import Flask, render_template


app = Flask(__name__)

#@app.route('/')
#def principal():
#   return "Bienvenidos a mi pagina WEB - aprende pyhton"

#@app.route('/contactos')
#def conctactos():
#    return "Esta es la pagina de contactos"

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/lenguajes')
def mostrarlenguaje():
    milenguajes=('PHP','Python','JAVA','C#','Ruby','JavaScript','Go')
    return render_template('lenguajes.html', lenguajes=milenguajes)

if __name__ == '__main__':
    app.run(debug=True, port=5017)

