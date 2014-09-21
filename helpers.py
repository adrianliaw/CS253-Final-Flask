from regexconverter import *

def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def valid_password(password):
    USER_RE = re.compile(r"^.{3,20}$")
    return USER_RE.match(password)

def verify_password(password, verify):
    return password == verify

def valid_email(email):
    USER_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    return USER_RE.match(email) or email == ""

def make_salt():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))

def make_pw_hash(name, pw):
    salt = make_salt()
    h = hashlib.sha256((pw + salt + name).encode("utf-8")).hexdigest()
    return h + salt

def valid_pw(name, pw, h):
    salt = h[-10:]
    return hashlib.sha256((pw + salt + name).encode("utf-8")).hexdigest() == h[:-10]

def valid_session(user_id):
    if Users.find_one({"_id":ObjectId(user_id)}):
        return True
    return False

class NullObject:
    def __init__(self, **kwargs):
        for key in kwargs:
            self.__setattr__(key, kwargs[key])