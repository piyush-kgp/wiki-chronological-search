import flask
import os
import chronological_search as chr

app = flask.Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def webpage():
    return flask.render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
    content = flask.request.get_json(silent = True)
    search_text = content['search_text']
    search_result = chr.wiki_search(search_text)
    if isinstance(search_result, chr.w.wikipedia.WikipediaPage):
        event_df =  chr.get_event_df(search_result, n = 10)
        return flask.jsonify({'valid_search': True, 'event_df': event_df})
    else:
        return flask.jsonify({'valid_search': False, 'search_result': search_result})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
