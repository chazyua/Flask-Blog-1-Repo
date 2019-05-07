from app import db, Login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Flask Login - User Mixin
# .is_aunthenticated - if user is logged in
# .is_active - if user's account is active
# .is_anonymous - if user is not logged
# .get_id() - returns the id of user

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(180))


    def __repr__(self):
        return f'<User: {self.name} | {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@Login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(70))
    content = db.Column(db.String(1000))
    author = db.Column(db.String())




