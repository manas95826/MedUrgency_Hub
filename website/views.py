from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required,current_user
from .models import patientdetails,User,hospitals
from . import db

views = Blueprint('views', __name__)
data = []

@views.route('/')
@login_required
def home():
    ff = hospitals(name="kukreja",key="qazxswedcvfr")
    db.session.add(ff)
    db.session.commit()
    return render_template("home.html",user=current_user)


@views.route('/details',methods=["GET","POST"])
@login_required
def details():
    if request.method == "POST":
        address = request.form.get("address")
        emergency = request.form.get("emergency")
        aadhar = request.form.get("aadhar")
        allergies = request.form.get("allergies")
        bloodgroup = request.form.get("bloodgroup")
        gender = request.form.get("gender")
        age = request.form.get("age")
        disease = request.form.get("disease")

        if len(emergency)<10:
            flash("Enter a valid phone number",category="error")

        elif not age.isnumeric():
            flash("Enter a valid Age",category="error")

        else:
          detail = patientdetails(address=address,emerphone=emergency,aadharno=aadhar,gender=gender,disease=disease,age=age,bloodgroup=bloodgroup,allergies=allergies,user_id=current_user.id)
          db.session.add(detail)
          db.session.commit()
          flash("details stored successfully",category="success")
          return  redirect(url_for("views.home"))

    return render_template("details.html",user=current_user)

@views.route('/getinfo/<userid>',methods=["GET","POST"])
def getinfo(userid):

      if request.method == "POST"  :
          key = request.form.get("key")
          print(key)
          hospital = hospitals.query.filter_by(key=key).first()

          if hospital:
               user = User.query.filter_by(id=userid).first()

               global data
               data = [user.name,user.patientdetail[0].address,user.patientdetail[0].emerphone,user.patientdetail[0].gender,user.patientdetail[0].aadharno,user.patientdetail[0].bloodgroup,user.patientdetail[0].disease,user.patientdetail[0].allergies,user.patientdetail[0].age,user.phone]
               return redirect(url_for("views.info"))
      return render_template("keyverify.html")


@views.route('/info')
def info():
    global data
    return render_template("hospital.html",data = data)