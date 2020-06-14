from flask import Flask,render_template,request,redirect,url_for,send_from_directory
import os
UPLOAD_FOLDER=os.path.abspath("./uploads")
#Aqui se van a guardar nuestros archivos 
app=Flask(__name__)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    #Texto del input
    textingres = request.form.get("descripcion")
    #Metodo seleccionado
    boton = request.form["metodo"]
    if textingres=="":
        output = request.files["adjunto"]
        if output.filename == "":
            return render_template("resultado.html", resultado="Archivo no seleccionado")
        filename=output.filename
        output.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        print("...............")
        direccion= os.path.join(app.config["UPLOAD_FOLDER"],filename)

        archivo = open(direccion,'r')
        for linea in archivo.readlines():
            print (linea)
        archivo.close()
        #Texto del archivo 
        return render_template("resultado.html", resultado=linea+"  "+boton)
    else:
        return render_template("resultado.html", resultado=textingres+"  "+boton)

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)