from flask import Flask, render_template
app = Flask(__name__)
todo = []



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_task')
def add_task(task):
    todo.append(task)
    return render_template('add-task.html', todo_list==todo)

if __name__ =="__main__":
    app.run(debug=True)

#bonus 1
#ცეცხლა?(idk)
#bonus 2
#ერთნაირია(sikvdils shexvda?)
#bonus 3
#ნესტანი(ერისთავის შვილიშვილი)
#bonus 4
#ნაკლების დაწერაც შეიძლებოდა