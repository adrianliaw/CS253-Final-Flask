from imports import *

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGOSOUP_URL")
app.config["MONGO_DBNAME"] = "cc_jtMPaDVgCNde"
app.secret_key = '\xfa\xde\x02\xa6^\xd9\xfb\xcd\x0e\x7f\xfc\xe9\xa4\x15\x9e\x14\x90i\x95\xa6\xfd-\x96\xb3'
mongo = PyMongo(app)
with app.app_context():
    Pages = mongo.db.pages
    Users = mongo.db.users