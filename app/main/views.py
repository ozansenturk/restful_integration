from app.main import bp
from flask import render_template,request, url_for,current_app,flash, redirect
from app.main.forms import TextForm

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@bp.route('/text', methods=['GET', 'POST'])
def text():
    form = TextForm()
    lemmitized = ""

    if form.validate():
        if form.text_option.data == 'lemmitize':
            flash('Your text is lemmitized!')


        elif form.text_option.data == 'pos_tag':
            flash('Your text is pos_tagged!')


        else:
            flash('Your entities extracted!')



        # return redirect(url_for('main.index'))

    return render_template('text_analytics.html', form=form, processed = lemmitized)





