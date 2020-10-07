from defect_app import db, login_manager
from flask import current_app
from flask_login import UserMixin
import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
        password = db.Column(db.String(60), nullable=False)
        posts = db.relationship('Post', backref='author', lazy=True)
        configs = db.relationship('Analyzer_config', backref='author', lazy=True)

        def get_reset_token(self, expires_sec=1800):
            s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
            return s.dumps({'user_id':self.id}).decode('utf-8')

        @staticmethod
        def verify_reset_token(token):
            s = Serializer(current_app.config['SECRET_KEY'])
            try:
                user_id = s.loads(token)['user_id']
            except:
                return None
            return User.query.get(user_id)

        def __repr__(self):
            return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow()+datetime.timedelta(hours=-3))
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        def __repr__(self):
            return f"Post('{self.title}','{self.date_posted}')"

class Image_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bobina = db.Column(db.String(15), nullable=False)
    linea = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(60), nullable=False)
    filepath = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return f"Image('Bobina:{self.bobina}','Linea:{self.linea}','Filename:{self.filename}','{self.date_posted}')"

class Analyzer_config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)#+datetime.timedelta(hours=-3))
    model_path = db.Column(db.String(200), nullable=False)
    labels_path = db.Column(db.String(200), nullable=False)
    input_images_path = db.Column(db.String(200), nullable=False)
    output_images_path = db.Column(db.String(200), nullable=False)
    image_saving = db.Column(db.Boolean, nullable=False, default=True)
    generate_template = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"ID: {self.id}, \
        Config('Title: {self.title},\
        Description: {self.description}, \
        Date: {self.date_created}, \
        Model_path: {self.model_path}, \
        Labels_path: {self.labels_path}, \
        Input images path: {self.input_images_path}, \
        Output images path: {self.output_images_path}, \
        Image saving: {self.image_saving}, \
        Generate template: {self.generate_template}')"
