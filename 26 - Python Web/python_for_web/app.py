# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
from collections import Counter
from statistics import mean
import pandas as pd
import os  # importing operating system module

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def countWords(text):
    text = text.lower()
    skips = [".", ", ", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = dict(Counter(text.split(" ")))
    return word_counts


@app.route('/')  # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result')
def result():
    content = request.args.get('content', None)

    dict_words = countWords(content)
    df = pd.DataFrame([dict_words], index=['Number of reps'])
    df = df.transpose()
    nwords = sum(dict_words.values())
    m = max(dict_words, key=dict_words.get)
    nch = len(content)
    ld = len(dict_words)/nwords

    return render_template('result.html', nwords=nwords, m=m, nch=nch, ld=ld,
                           tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for('result', content=content))


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
