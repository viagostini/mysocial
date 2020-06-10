from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vinicius'}
    posts = [
        {
            'author': {'username': 'João'},
            'body': 'Hoje é um ótimo dia para estudar microserviços.'
        },
        {
            'author': {'username': 'Marcelo'},
            'body': 'fastapi é a melhor coisa que já vi!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requisitado por usuário {form.username.data},'
              + f' manter_conectado={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
