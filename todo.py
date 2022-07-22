from flask import Flask,render_template,flash,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:given@localhost:5432/todoapp'
# app.config['SQLALCHEMY_DATABASE_URI'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(),nullable=False)
def __repr__(self):
    return f"<todo ID:{self.id}, content:{self.content}>"


@app.route('/todos/create',methods = ['POST'])
def create_todo():
    content1 = request.form.get('content')
    new_content = Todo(content = content1)
    db.session.add(new_content)
    db.session.commit()
    return redirect(url_for('index'))

db.create_all()    

@app.route("/")
def index():
    return render_template('index.html',todos = Todo.query.all())

#  i will come back to this (:
# @app.route('/todos/delete/<id>',methods=['GET','POST'])
# def delete(id):
#     todos = Todo.query.get(id)
#     db.session.delete(todos)
#     db.session.commit()  
# #     flash('todo deleted successfully')




# # this is the debugging statement







if __name__== '__main__':
    app.run(debug=True)