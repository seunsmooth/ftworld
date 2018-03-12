from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect
y= ':smile:'
user = {'username': 'Awoga'}
s = {"content" : y }
d = {"content" : ":drunk:"}
ff = {"content" : ":fearful_face:"}
t = {"content" : ":electric_light_bulb:"}
#t = {"content" : ":electric_light_bulb:"}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user, s=s, t=t, d=d, ff=ff)
   #return render_template_string(s=s, t=t)

@app.route('/index/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', form=form, user=user)

