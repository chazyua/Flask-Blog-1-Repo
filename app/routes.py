from app import app, db
from flask import render_template, redirect, url_for, request, flash
from app.forms import RegistrationForm, LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from werkzeug.urls import url_parse


@app.route("/") # the home route
def index():
    context = {
        'names' : ['Derek', 'Artem', 'Lakshmi', 'Vick', 'Shibani']
    }
    return render_template('index.html', **context)

@app.route("/about") # the about page
def about():
    return render_template('about.html')

@app.route("/contact") # the random page
def contact():
    return render_template('contact.html')

@app.route('/register', methods={'GET', 'POST'} )
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    context = {
        'form' : form
    }
    if form.validate_on_submit():
        u = User(
            name = form.name.data,
            email = form.email.data
        )
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('User has been registered', 'alert alert-info')
        return redirect(url_for('login'))
    return render_template('register.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    context = {
        'form' : form
    }
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('Email or Username are incorrect', 'alert alert-danger')            
            return redirect(url_for('login'))
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('profile')
            flash('User has been logged in succesfully', 'alert alert-info')        
            return redirect(next_page)
    return render_template('login.html', **context)

@app.route('/logout')
def logout():
    logout_user()
    flash('User has been logged out', 'alert alert-info')
    return redirect(url_for('login'))

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = PostForm()
    context = {
       'form': form,
       'posts' : Post.query.all()
    }
    if form.validate_on_submit():
        p = Post(
            title = form.title.data,
            content = form.content.data,
            author = form.author.data
        )
        db.session.add(p)
        db.session.commit()
        flash('Post has been created', 'alert alert-info')
        return redirect(url_for('profile'))
    return render_template('new_post.html', **context)

# @app.route("/new_post", methods=['GET', 'POST'])
# @login_required
# def new_post():
#     form = PostForm()
#     context = {
#        'form': form,
#        'posts' : Post.query.all()
#     }
#     if form.validate_on_submit():
#         p = Post(
#             title = form.title.data,
#             content = form.content.data,
#             author = form.author.data
#         )
#         db.session.add(p)
#         db.session.commit()
#         flash('Post has been created', 'alert alert-info')
#         return redirect(url_for('profile'))
#     return render_template('new_post.html', **context)
    