from extensions import db #importing database
from werkzeug.security import generate_password_hash, check_password_hash

#USER MODEL
class User(db.Model):
    #this key is unique for each user
    id = db.Column(db.Integer, primary_key=True)

    # username (must be unique)
    username = db.Column(db.String(100), unique=True, nullable=False)

    # hashed password (never store plain text password)
    password_hash = db.Column(db.String(200), nullable=False)

    # function to set password (hashing)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # function to check password during login
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)