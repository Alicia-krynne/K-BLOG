from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(600),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(600),unique = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)


    def save_u(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}'


    '''
    class Role(db.Model):
        __tablename__ = 'roles'

        id = db.Column(db.Integer,primary_key = True)
        name = db.Column(db.String(255))
        users = db.relationship('User',backref = 'role',lazy="dynamic")


        def __repr__(self):
            return f'User {self.name}'
    '''

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50),nullable = False)
    subtitle = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='blog',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='blog',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    
    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    
    def __repr__(self):
        return f'Blog {self.post}'

class Quote:
    """
    Quote class to define Quote Objects
    """

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False)

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments

    @login_manager.user_loader

    def __repr__(self):
        return f'comment:{self.comment}'
       

    

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote


    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'
class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

   