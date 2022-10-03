from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello", times=5)

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

@app.route('/lists')
def render_lists():
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template('lists.html', random_numbers = [3,1,5], students = student_info)



if __name__=="__main__":   
    app.run(debug=True)    
