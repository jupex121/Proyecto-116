# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Emilio" # escribe tu nombre
    age = "15" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route("/padre")
def home2():

    name = "Raúl" # escribe su nombre
    age = "45" # escribe su edad

    return render_template('father.html' , name = name , age = age)

# define la ruta a la página web de tu madre.
@app.route("/madre")
def home3():

    name = "Dora" # escribe su nombre
    age = "55" # escribe su edad

    return render_template('mother.html' , name = name , age = age)

# define la ruta a la página web de tus amigos.
@app.route("/amigo")
def home4():

    name = "Santiago" # escribe su nombre
    age = "15" # escribe su edad

    return render_template('friend.html' , name = name , age = age)

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
