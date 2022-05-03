from flask import render_template
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def articles():
    articles = get_articles()
    title = 'Tantalizers'

    return render_template('articles.html', title = title, articles = articles)

@main.route('/sources')
def sources():
    sources = get_sources()
    title = 'TheSource'
    return render_template('source.html', title = title,sources = sources)

