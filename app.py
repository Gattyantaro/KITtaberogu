from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50) , unique = True)
    content = db.Column(db.String(200) , unique = True)

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("add"))

@app.route("/post", methods=["GET", "POST"])
def post():
    return render_template("post.html")

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    content = request.form.get("content")
    new_post = Post(title = title , content = content)
    db.session.add(new_post)
    db.session.commit()
    dbtakes = Post.query.all()
    return render_template("KITtop.html" , dbtakes = dbtakes)


@app.route("/delete", methods=["POST"])
def delete():
    post = Post.query.filter_by(id=Post).first()
    db.session.delete(post)
    db.session.commit()
    return render_template("KITtop.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
