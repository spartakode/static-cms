from flask import session,url_for,request,redirect,render_template
from . import application

from .controllers import RegisterController, LoginController, PostController, ViewPostController, EditPostController
from .core.user import UserRetrieval, UserAuthentication
from .data.sqlite import UserDataStrategy

BASEPATH = "/blogadmin/"
@application.route(BASEPATH)
def index():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("admin"))

@application.route(BASEPATH+"register/", methods=['GET', 'POST'])
def register():
    if UserRetrieval.doesAUserExist(UserDataStrategy):
        return redirect(url_for("login"))
    else:
        if request.method == "GET":
            return render_template("register.html")
        else:
            RegisterController.registerUser(request.form)
            return redirect(url_for("login"))

@application.route(BASEPATH+"login/", methods=['GET', 'POST'])
def login():
    if not UserRetrieval.doesAUserExist(UserDataStrategy):
        return redirect(url_for("register"))
    if 'username' in session:
        return redirect(url_for("index"))
    else:
        if request.method == "GET":
            return render_template("login.html")
        else:
            loginResult = LoginController.loginUser(request.form)
            if loginResult:
                session['username'] = request.form['username']
                return redirect(url_for("index"))
            else:
                return redirect(url_for("login"))

@application.route(BASEPATH+"admin/", methods=['GET', 'POST'])
def admin():
    if 'username' not in session:
        return redirect(url_for("login"))
    return render_template('admin.html')

@application.route(BASEPATH+"createpost/", methods=['GET', 'POST'])
def createpost():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        if request.method == "GET":
            return render_template('createpost.html',action="Create Post",
                    saveAction = "Save Post",
                    formAction = url_for('createpost'))
        else:
            PostController.savePost(request.form)
            return redirect(url_for('admin'))
@application.route(BASEPATH + "viewposts/", methods=['GET'])
def viewposts():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        allPosts = ViewPostController.getAllPosts()
        return render_template('viewposts.html', posts = allPosts)
@application.route(BASEPATH + "editpost/", methods=['POST'])
def editpost():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        postUrl = request.form['posturl']
        print("post url is: " + postUrl)
        post = EditPostController.getPostInMarkdown(postUrl)
        return render_template('createpost.html', postTitle = post.postTitle,
                postLink = post.postLink,
                postBody = post.postBody,
                postUrl = post.postUrl,
                action = "Edit Post",
                saveAction = "Update Post",
                formAction = url_for('saveUpdatedPost')
                )
@application.route(BASEPATH + "editpost/update", methods=['POST'])
def saveUpdatedPost():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        EditPostController.updatePost(request.form)
        return redirect(url_for('viewposts'))
