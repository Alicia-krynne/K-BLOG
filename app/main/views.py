from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,Blog,Comment,Upvote,Downvote
from .forms import UpdateProfile,BlogForm,CommentForm

# Views
@main.route('/')
def index():
    blogs = Blog.query.all()
    food = Blog.query.filter_by(category = 'food').all() 
    music= Blog.query.filter_by(category = 'music').all()
    fashion= Blog.query.filter_by(category = 'fashion').all()
    return render_template('index.html', food = food,music=music, fashion= fashion)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_Blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_Blog_object = Blog(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_Blog_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('new_Blog.html', form = form)

@main.route('/comment/<int:Blog_id>', methods = ['POST','GET'])
@login_required
def comment(Blog_id):
    form = CommentForm()
    Blog = Blog.query.get(Blog_id)
    all_comments = Comment.query.filter_by(Blog_id = Blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        Blog_id = Blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,Blog_id = Blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', Blog_id = Blog_id))
    return render_template('comments.html', form =form, Blog = Blog,all_comments=all_comments)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)


@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_Bloges = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for Blog in get_Bloges:
        to_str = f'{Blog}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, Blog_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    Blog = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in Blog:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, Blog_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))
