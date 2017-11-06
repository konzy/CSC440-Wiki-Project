"""
    Routes
    ~~~~~~
"""
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import request
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from string import replace

from wiki.core import Processor
from wiki.web.forms import EditorForm
from wiki.web.forms import LoginForm
from wiki.web.forms import SearchForm
from wiki.web.forms import URLForm
from wiki.web import current_wiki
from wiki.web import current_users
from wiki.web import base_addr ##for use in to_pdf etc
from wiki.web.user import protect

import smtplib
from string import Template


bp = Blueprint('wiki', __name__)


@bp.route('/')
@protect
def home():
    page = current_wiki.get('home')
    if page:
        return display('home')
    return render_template('home.html')


@bp.route('/topdf/')
@protect #this just wraps the function to make sure the user is authenticated
def toPdf():
    ##get urls
    index = current_wiki.index()
    for page in index:
        print url_for('wiki.display', url=page.url)
        ##TODO store these in something, we need url and path to the .md file
    ##get current url
    ref = request.referrer
    ref = ref.replace(base_addr, '')
    ##TODO match current url to that of a page from the index, and thus a path to its markdown file
    ##TODO make sure that we deal with the edge case of home having a special url ( '/' )
    ##TODO call pandoc to make pdf with this path
    return redirect(request.referrer) ##don't navigate away from the page


def email(page):
    #get the contacts to send email to
    names = []
    emails = []
    with open("content/contacts.txt", mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            if(a_contact.split()[2] == page):
                names.append(a_contact.split()[0])
                emails.append(a_contact.split()[1])

    #get the message ready to send to the contacts
    with open("content/message.txt", 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    message_template = Template(template_file_content)

    # set up the SMTP server
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login("megatroniki2017@gmail.com", "megatron1234")

    #send the email
    sender = 'megatroniki2017@gmail.com'
    receivers = emails

    message = message_template.substitute(PAGE=page)

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"


@bp.route('/index/')
@protect
def index():
    pages = current_wiki.index()
    return render_template('index.html', pages=pages)


@bp.route('/<path:url>/')
@protect
def display(url):
    page = current_wiki.get_or_404(url)
    return render_template('page.html', page=page)


@bp.route('/create/', methods=['GET', 'POST'])
@protect
def create():
    form = URLForm()
    if form.validate_on_submit():
        return redirect(url_for(
            'wiki.edit', url=form.clean_url(form.url.data)))
    return render_template('create.html', form=form)


@bp.route('/edit/<path:url>/', methods=['GET', 'POST'])
@protect
def edit(url):
    page = current_wiki.get(url)
    form = EditorForm(obj=page)
    if form.validate_on_submit():
        if not page:
            page = current_wiki.get_bare(url)
        form.populate_obj(page)
        page.save()
        flash('"%s" was saved.' % page.title, 'success')
        email(url)
        return redirect(url_for('wiki.display', url=url))
    return render_template('editor.html', form=form, page=page)


@bp.route('/preview/', methods=['POST'])
@protect
def preview():
    data = {}
    processor = Processor(request.form['body'])
    data['html'], data['body'], data['meta'] = processor.process()
    return data['html']


@bp.route('/move/<path:url>/', methods=['GET', 'POST'])
@protect
def move(url):
    page = current_wiki.get_or_404(url)
    form = URLForm(obj=page)
    if form.validate_on_submit():
        newurl = form.url.data
        current_wiki.move(url, newurl)
        return redirect(url_for('wiki.display', url=newurl))
    return render_template('move.html', form=form, page=page)


@bp.route('/delete/<path:url>/')
@protect
def delete(url):
    page = current_wiki.get_or_404(url)
    current_wiki.delete(url)
    flash('Page "%s" was deleted.' % page.title, 'success')
    return redirect(url_for('wiki.home'))


@bp.route('/tags/')
@protect
def tags():
    tags = current_wiki.get_tags()
    return render_template('tags.html', tags=tags)


@bp.route('/tag/<string:name>/')
@protect
def tag(name):
    tagged = current_wiki.index_by_tag(name)
    return render_template('tag.html', pages=tagged, tag=name)


@bp.route('/search/', methods=['GET', 'POST'])
@protect
def search():
    form = SearchForm()
    if form.validate_on_submit():
        results = current_wiki.search(form.term.data, form.ignore_case.data)
        return render_template('search.html', form=form,
                               results=results, search=form.term.data)
    return render_template('search.html', form=form, search=None)


@bp.route('/user/login/', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = current_users.get_user(form.name.data)
        login_user(user)
        user.set('authenticated', True)
        flash('Login successful.', 'success')
        return redirect(request.args.get("next") or url_for('wiki.index'))
    return render_template('login.html', form=form)


@bp.route('/user/logout/')
@login_required
def user_logout():
    current_user.set('authenticated', False)
    logout_user()
    flash('Logout successful.', 'success')
    return redirect(url_for('wiki.index'))


@bp.route('/user/')
def user_index():
    pass


@bp.route('/user/create/')
def user_create():
    pass


@bp.route('/user/<int:user_id>/')
def user_admin(user_id):
    pass


@bp.route('/user/delete/<int:user_id>/')
def user_delete(user_id):
    pass

"""
    Error Handlers
    ~~~~~~~~~~~~~~
"""


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

