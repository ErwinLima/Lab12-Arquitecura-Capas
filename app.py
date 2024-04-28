from flask import Flask, render_template, request
import mysql.connector
from gpiozero import LED

led = LED(18)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/encender',methods=['GET','POST'])
def encender():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'add':
                print('encendiendo')
                led.on()
                insertar('Se encendio la luz')
            return render_template('main.html')
        return render_template('main.html')
    except:
        return render_template('main.html')

@app.route('/apagar',methods=['GET','POST'])
def apagar():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'add':
                print('apagando')
                led.off()
                insertar('Se apago la luz')
            return render_template('main.html')
        return render_template('main.html')
    except:
        return render_template('main.html')

def insertar( msg : str):
    mydb = mysql.connector.connect(
        host='localhost',
        database='pruebas_db',
        user='el1158120',
        password='12345',
        charset='latin1'
        )

    mycursor = mydb.cursor()

    query = """INSERT INTO LIGHTSPLEASE (ACCION) VALUES (%s)"""
    record = (msg)
    mycursor.execute(query, (record,))
    mydb.commit()
    print("Se inserto correctamente en LIGHTSPLEASE")
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Se cerro la conexión")



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=83, debug=True)
