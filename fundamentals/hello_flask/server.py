from flask import Flask  
app = Flask(__name__)  

@app.route('/')          
def hello_world():
    return 'Hello World!' 
@app.route('/success')
def success():
    return "success"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<insertword>')
def say(insertword):
    print(insertword)
    return f"Hi {insertword}"

@app.route('/repeat/<int:insertnumber>/<insertword>')
def repeat(insertnumber, insertword):
    print(insertnumber, insertword)
    return insertword * insertnumber

if __name__=="__main__":   
    app.run(debug=True)    
