from flask import session,url_for,request,redirect,render_template
from . import application

from .controllers import *
from .core.user import UserRetrieval, UserAuthentication
from .data.sqlite import UserDataStrategy

BASEPATH = "/blogadmin/"
@application.route(BASEPATH)
def index():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        return render_template('createpost.html')

@application.route(BASEPATH+"register/", methods=['GET', 'POST'])
def register():
    if UserRetrieval.doesAUserExist(UserDataStrategy):
        return redirect(url_for("login"))
    else:
        if request.method == "GET":
            return render_template("register.html")
        else:
            RegisterController.registerUser(request.form)

@application.route(BASEPATH+"login/", methods=['GET', 'POST'])
def login():
    if not UserRetrieval.doesAUserExist(UserDataStrategy):
        return redirect(url_for("register"))
    if 'username' in session:
        return redirect(url_for(index))
    else:
        return render_template("login.html")
