from helpers import *

@app.route("/")
def redirect_to_home():
    if Pages.find({"page_id":"home"}).count() == 0:
        Pages.insert({
            "page_id": "home", 
            "content": "# Welcome To The Final!", 
            "created": datetime.now()
        })
    return redirect("/home")

@app.route('/<regex("(?:[a-zA-Z0-9_-]+/?)*"):uid>')
def wikipage(uid):
    pages = Pages.find({"page_id":uid}).sort("created", -1)
    if request.args.get("v") != None:
        if int(request.args.get("v")) in range(pages.count()):
            page = pages[int(request.args["v"])]
        elif pages:
            page = pages[0]
        else:
            page = None
    else:
        try:
            page = pages[0]
        except IndexError:
            page = None
    user = Users.find_one({"_id":ObjectId(session.get("user_id"))})
    if page:
        return render_template(
            "wikipage.html", 
            page = page, 
            md2html = markdown2.markdown, 
            user = user
        )
    else:
        return redirect("/_edit/{}".format(uid))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = str(request.form["username"])
        password = str(request.form["password"])
        verify = str(request.form["verify"])
        email = str(request.form["email"])
        errs = {}
        if not valid_username(username):
            errs["er_username"] = "Invalid username"
        if not valid_password(password):
            errs["er_password"] = "Invalid password"
        else:
            if not verify_password(password, verify):
                errs["er_verify"] = "Password doesn't match"
        if not valid_email(email):
            errs["er_email"] = "Invalid email"
        if "er_username" not in errs:
            if Users.find_one({"username":username}):
                errs["er_username"] = "User already exists"
        if errs:
            errs["username"] = username
            errs["email"] = email
            return render_template("signup.html", **errs)
        else:
            user_id = Users.insert({
                "username": username, 
                "password": make_pw_hash(username, password), 
                "email": email
            })
            session["user_id"] = str(user_id)
        return redirect("/home")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = str(request.form["username"])
        password = str(request.form["password"])
        error = ""
        usr = Users.find_one({"username":username})
        if not usr:
            error = "Invalid login."
        else:
            if not valid_pw(username, password, usr["password"]):
                error = "Invalid login."
        if error:
            return render_template("login.html", error=error, username=username)
        else:
            session["user_id"] = str(usr["_id"])
            return redirect("/home")

@app.route('/_edit/<regex("(?:[a-zA-Z0-9_-]+/?)*"):uid>', methods=["GET", "POST"])
def edit(uid):
    if request.method == "GET":
        pages = Pages.find({"page_id":uid}).sort("created", -1)
        if request.args.get("v") != None:
            if int(request.args.get("v")) in range(pages.count()):
                page = pages[int(request.args["v"])]
            elif pages:
                page = pages[0]
            else:
                page = NullObject(page_id=uid, content="")
        elif pages.count():
            page = pages[0]
        else:
            page = NullObject(page_id=uid, content="")
        user = Users.find_one({"_id":ObjectId(session.get("user_id"))})
        if valid_session(session.get("user_id")):
            return render_template("edit.html", page=page, user=user)
        else:
            return redirect("/login")
    else:
        if request.form["save_or_preview"] == "PREVIEW":
            content = request.form["content"]
            page_id = uid
            page = NullObject(content=content, page_id=page_id)
            user = Users.find_one({"_id":ObjectId(session.get("user_id"))})
            return render_template("edit.html", page=page, user=user, md2html=markdown2.markdown)
        elif request.form["save_or_preview"] == "SAVE":
            content = request.form["content"]
            page_id = uid
            page = Pages.find_one({"$query":{"page_id":page_id}, "$orderby":{"created":-1}})
            if page:
                if page["content"] == content:
                    return redirect("/{}".format(page_id))
            Pages.insert({
                "page_id": page_id, 
                "content": content, 
                "created": datetime.now()
            })
            return redirect("/{}".format(page_id))

@app.route('/_history/<regex("(?:[a-zA-Z0-9_-]+/?)*"):uid>')
def history(uid):
    pages = Pages.find({"$query":{"page_id":uid}, "$orderby":{"created":-1}})
    user = Users.find_one({"_id":ObjectId(session.get("user_id"))})
    return render_template("history.html", pages=pages, user=user, page=uid)
