from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')         
def eightbyeight():
    return render_template('index.html')  

@app.route('/4')         
def fourbyfour():
    return render_template('index2.html')  

@app.route('/<num1>/<num2>')          
def repeatrows (num1, num2): 
    return render_template("index3.html", across = int(num1), down = int(num2))

if __name__=="__main__":   
    app.run(debug=True)  