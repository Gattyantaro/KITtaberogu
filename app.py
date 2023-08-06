from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50) , unique = True)
    todo = db.Column(db.String(200) , unique = True)

@app.route("/", methods=["GET"])
def index():
    return render_template("KITtop.html")

@app.route("/post", methods=["GET", "POST"])
def post():
    post_list = todo.query.all()
    return render_template("index.html", post_list = post_list)

@app.route("/add", methods=["POST"])
def add():
    store_title = request.form.get("store_title")
    post = request.form.get("post")
    new_post = Post(title = store_title)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for("post"))


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("post"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
