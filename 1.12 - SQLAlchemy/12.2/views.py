from flask import render_template, request, redirect

from main import app, db
from models import BlogPosts

@app.route('/', methods=['GET', 'POST'])
def info():
    blogposts= BlogPosts.query.all()
    return render_template('info.html', blogposts=blogposts)

@app.route('/new-post', methods=['POST'])
def new_post():
    content = request.form['content']
    subj = request.form['subject']
    post = BlogPosts(text=content, subject=subj)
    db.session.add(post)
    db.session.commit()
    return redirect('/')