import wikipedia as w
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
import pandas as pd
import datefinder
import itertools

def wiki_search(search_term):
    try:
        return w.page(search_term)
    except w.exceptions.DisambiguationError as e:
        return e.options

def get_event_df(wiki_page, n = 10):
    lines = [line.rstrip() for line in nltk.sent_tokenize(wiki_page.content)]
    lines = [re.sub(r'=[0-9a-zA-Z_\D]*=', r'', line) for line in lines]
    lines = [re.sub(r'===a-zA-Z===', r'', line) for line in lines]
    lines = [re.sub(r'\n', r'', line) for line in lines]
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english',decode_error='ignore' )
    tfidf_vectorizer.fit(lines)
    events = [line for line in lines if isNotEmpty(datefinder.find_dates(line))]
    dates = [sorted(list(datefinder.find_dates(event)))[-1] for event in events]
    validDates = [date.year<2018 and date.year>1500 for date in dates]
    events = list(itertools.compress(events, validDates))
    dates = list(itertools.compress(dates, validDates))
    scores = [sum(tfidf_vectorizer.transform([e]).toarray().flatten()) for e in events]
    max_scores_idx = np.array(scores).argsort()[-n:][::-1]
    top_events = [events[idx] for idx in max_scores_idx]
    top_years = [dates[idx].year for idx in max_scores_idx]
    edf = pd.DataFrame({'Year': top_years, 'Event': top_events})
    edf = edf.sort_values(by='Year').reset_index(drop=True)
    # with pd.option_context('display.max_colwidth', -1, 'display.colheader_justify','center'):
    #         return edf.to_html(index=False, na_rep='-', justify='center')
    with pd.option_context('display.max_colwidth', -1):
            return edf.to_html(index=False, na_rep='-')
            
def isNotEmpty(iterable):
    try:
        next(iterable)
        return True
    except StopIteration:
        return False
