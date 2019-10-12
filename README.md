# Wikipedia Chronological Search

This is a small project to demonstrate Wikipedia Chronological Search.

It lets you search for a person on Wikipedia, comes up with the page you want, finds top 10 important events in their life and displays them chronologically.

### Update (12/10/2019):
<b> The application is live at <u><https://search-wiki-chrono.herokuapp.com>
</u></b>


<img src = "Screenshot 2019-10-12 at 12.50.18 PM.png"/>


## Running on your own machine
```
docker run -d -p 8000:8000 piyushkgp/wiki-chrono
```
Go over to <http://localhost:8000> and you should see the application
running.

## Local development
```
git clone https://github.com/piyush-kgp/wikipedia-chronological-search
cd wikipedia-chronological-search
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
## Heroku Deployment
[Heroku](http://heroku.com) offers free deployment of containerzied applications. The Heroku version of this application is in `heroku` branch (slightly different directory structure and uses `gunicorn`).
