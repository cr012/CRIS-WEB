#importamos flask

from flask import Flask, render_template

#creamos una variable u objeto(app) para decir que este archivo va a arrancar la aplicacion
#render_template son archivos html que queremos que el usuario vea

app = Flask(__name__)

#damos una ruta con el metodo (route) para la primera pagina

@app.route('/')

#cuando un usuario entre a la pag principal retornara algo

def home():
    return render_template('home.html')

#dentro de return,en vez de poner un texto podemos anexar una pagina html
#tendremos que hacer que nuestra aplicacion siempre se quede a la escucha ante cualquier peticion
#hacemos una validacion para comprobar que estamos en el archivo principal y que sea un archivo de ejecucion y no como un modulo
#en return,podemos escribir un texto o ponemos un archivo que creemos de html.

@app.route('/about')
def about():
    return render_template('about.html')
#podemos crear otra routa para que el usuario pueda ver

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/descripcion_problema')
def descripcion_problema():
    return render_template('descripcion_problema.html')

@app.route('/opiniones')
def opiniones():
    return render_template('opiniones.html')

if __name__ == ('__main__'):
     app.run(debug=True)

     
#para verlo en la interfaz grafica nos vamos a la consola y ejecutamos el archivo index.py
#el debug=True es para que no tengamos que reiniciar a cada momento la terminal      

