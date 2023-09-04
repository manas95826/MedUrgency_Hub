from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user
import qrcode
import shutil

auth = Blueprint('auth', __name__)


@auth.route('/login',methods = ['GET','POST'])
def login():

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password,password):
                flash("Logged in successfully ",category="success")
                login_user(user,remember = True)
                return redirect(url_for("views.home"))
            else:
               flash("Incorrect password",category="error")
        else:
           flash("email does not exist",category="error")



    return render_template("login.html")


@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":

        email = request.form.get("email")
        phone = request.form.get("phone")
        name = request.form.get("name")
        password = request.form.get("password")


        if len(phone) < 10 :
            flash("Invalid phone number",category="error")

        elif len(password) < 7:
             flash("Password too short",category="error")
        elif len(name) < 2 :
            flash("Name must be greater than 1 char !!",category="error")

        else:
          user = User.query.filter_by(email=email).first()

          if not user:
            new_user = User(email=email,name=name,phone=phone,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            id = current_user.id
            g = qrcode.make("https://medurgencyhub.onrender.com/getinfo/{}".format(id))
            name = '{}.png'.format(id)
            g.save(name)
            shutil.move(fr'{name}','website/static/')

            return redirect(url_for("views.details"))
            flash("Account Created now enter your details",category="success")
          else:
             flash("email already exists",category="error")

    return render_template("signup.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logout successful",category="success")
    return redirect(url_for("auth.login"))