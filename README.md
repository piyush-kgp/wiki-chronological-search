# Wikipedia Chronological Search

This is a small project to demonstrate Wikipedia Chronological Search. It searches Wikipedia for a search term, comes up with a page, finds events from the page and sorts these events by importance using TF-IDF and then shows the top 10 results sorted by chronological order (Latest comes last). If there are multiple Wikipedia pages, you'll be asked to select one of the options from a dropdown.

<img src = "Screen Shot 2018-12-03 at 4.04.11 AM.png"/>

The website is live at [http://chronologically.pythonanywhere.com/](http://chronologically.pythonanywhere.com/)

## Reproducing results
Make sure to install dependencies and simply run this:

```python app.py```

## Dependencies
```
Flask
nltk
scikit-learn
wikipedia
numpy
pandas
datefinder
```

### Built with
  <ul align="left">
    <li>
      <a href="https://www.python.org/">Python</a> Backend - <a href="http://flask.pocoo.org/">Flask</a>, <a href="http://www.nltk.org/">NLTK</a>, <a href="https://scikit-learn.org">Scikit-Learn</a>,   <a href="https://wikipedia.readthedocs.io/">Wikipedia</a></li>
    <li>HTML Frontend - <a href="https://jquery.com/">JQuery</a>, <a href="https://www.javascript.com/">JS</a></li>
</ul>


## Deployment on pythonanywhere:
```
git clone https://github.com/piyush-kgp/wikipedia-chronological-search
cd wikipedia-chronological-search
pip3 install -r requirements.txt
python3 -c "import nltk; nltk.download('punkt')"
```
After this, set your web-app path to ~/wikipedia-chronological-search/app.py. Also comment the last line (`app.run`).
