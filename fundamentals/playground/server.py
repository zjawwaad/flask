from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/')           
def hello_world():
    return 'Hello World!'


@app.route('/play')          
def boxes():
    return render_template("index.html")


@app.route('/play/<int:insertnumber>')          
def repeatboxes(insertnumber): 
    repeat=int(insertnumber)
    return render_template("index2.html", repeat=repeat)

@app.route('/play/<int:insertnumber>/<string:color>')          
def boxnumbers_colors(insertnumber, color): 
    repeat=int(insertnumber)
    color=color
    return render_template("index3.html", repeat=repeat, color=color)


if __name__=="__main__":
    app.run(debug=True)                   
