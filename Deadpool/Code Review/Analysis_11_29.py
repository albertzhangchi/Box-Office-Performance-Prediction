# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:39:54 2017

@author: Jack. Wang
"""
import os
import pandas as pd
import re
import numpy as np
import sys
import string
import nltk.data
import tweepy
import logging
import pickle
import matplotlib
from datetime import datetime
from dateutil import parser
from tweepy import OAuthHandler
from textblob import TextBlob
from nltk.corpus import stopwords
from gensim.models.word2vec import Word2Vec
from sklearn.cross_validation import train_test_split
from sklearn.metrics import average_precision_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import roc_auc_score
from sklearn import metrics, datasets, linear_model
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.sentiment import SentimentAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from scipy import stats
from scipy.stats.stats import *
from inspect import getargspec, ismethod, isclass, formatargspec
import statsmodels.api as sm
#from sklearn.neural_network import MLPClassifier
import statsmodels.api as sm

os.chdir('D:\Columbia-Course\CS-6998\Project')
os.getcwd()

corpus_13 = pd.read_csv('corpus_13.csv')
corpus_14 = pd.read_csv('corpus_14.csv')
corpus_15 = pd.read_csv('corpus_15.csv')
corpus_16 = pd.read_csv('corpus_16.csv')
corpus_17 = pd.read_csv('corpus_17.csv')
corpus_18 = pd.read_csv('corpus_18.csv')
corpus_19 = pd.read_csv('corpus_19.csv')
corpus_20 = pd.read_csv('corpus_20.csv')
corpus_21 = pd.read_csv('corpus_21.csv')
corpus_22 = pd.read_csv('corpus_22.csv')
corpus_23 = pd.read_csv('corpus_23.csv')
corpus_24 = pd.read_csv('corpus_24.csv')

corpus_23.columns.values
del corpus_13['Unnamed: 0']
del corpus_14['Unnamed: 0']
del corpus_15['Unnamed: 0']
del corpus_16['Unnamed: 0']
del corpus_17['Unnamed: 0']
del corpus_18['Unnamed: 0']
del corpus_19['Unnamed: 0']
del corpus_20['Unnamed: 0']
del corpus_21['Unnamed: 0']
del corpus_22['Unnamed: 0']
del corpus_23['Unnamed: 0'];del corpus_23['index']
del corpus_24['Unnamed: 0'];del corpus_24['index']

corpus_23, corpus_24 = train_test_split(corpus_23_24, test_size = 0.5, random_state=42)
corpus_23 = corpus_23.reset_index()
corpus_24 = corpus_24.reset_index()

###SUM of retweet
np.mean(corpus_13['retweets'])
retweets_13 = sum(corpus_13['retweets'])
retweets_14 = sum(corpus_14['retweets'])
retweets_15 = sum(corpus_15['retweets'])
retweets_16 = sum(corpus_16['retweets'])
retweets_17 = sum(corpus_17['retweets'])
retweets_18 = sum(corpus_18['retweets'])
retweets_19 = sum(corpus_19['retweets'])
retweets_20 = sum(corpus_20['retweets'])
retweets_21 = sum(corpus_21['retweets'])
retweets_22 = sum(corpus_22['retweets'])
retweets_23 = sum(corpus_23['retweets'])
retweets_24 = sum(corpus_24['retweets'])
retweets_25 = sum(corpus_25['retweets'])
retweets_26 = sum(corpus_26['retweets'])

###Mean of favorite
fav_13 = np.mean(corpus_13['favorites'])
fav_14 = np.mean(corpus_14['favorites'])
fav_15 = np.mean(corpus_15['favorites'])
fav_16 = np.mean(corpus_16['favorites'])
fav_17 = np.mean(corpus_17['favorites'])
fav_18 = np.mean(corpus_18['favorites'])
fav_19 = np.mean(corpus_19['favorites'])
fav_20 = np.mean(corpus_20['favorites'])
fav_21 = np.mean(corpus_21['favorites'])
fav_22 = np.mean(corpus_22['favorites'])
fav_23 = np.mean(corpus_23['favorites'])
fav_24 = np.mean(corpus_24['favorites'])
fav_25 = np.mean(corpus_25['favorites'])
fav_26 = np.mean(corpus_26['favorites'])

#Indicator
corpus_13['Indicator']= 'NA'
corpus_14['Indicator']= 'NA'
corpus_15['Indicator']= 'NA'
corpus_16['Indicator']= 'NA'
corpus_17['Indicator']= 'NA'
corpus_18['Indicator']= 'NA'
corpus_19['Indicator']= 'NA'
corpus_20['Indicator']= 'NA'
corpus_21['Indicator']= 'NA'
corpus_22['Indicator']= 'NA'
corpus_23['Indicator']= 'NA'
corpus_24['Indicator']= 'NA'
corpus_25['Indicator']= 'NA'
corpus_26['Indicator']= 'NA'

#Google Trends
corpus_13['GT']= 77
corpus_14['GT']= 100
corpus_15['GT']= 99
corpus_16['GT']= 77
corpus_17['GT']= 59
corpus_18['GT']= 51
corpus_19['GT']= 45
corpus_20['GT']= 47
corpus_21['GT']= 62
corpus_22['GT']= 60
corpus_23['GT']= 39
corpus_24['GT']= 30
corpus_25['GT']= 28
corpus_26['GT']= 25


i=0
corpus_13['Compound_Score']
while i < len(corpus_13['retweets']):
    if corpus_13['Compound_Score'][i] > 0.0516:
        corpus_13['Indicator'][i] = 'PP'
    elif corpus_13['Compound_Score'][i] < -0.0516:
        corpus_13['Indicator'][i] = 'Neg'
    else:
        corpus_13['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_14['Compound_Score']
while i < len(corpus_14['retweets']):
    if corpus_14['Compound_Score'][i] > 0.0516:
        corpus_14['Indicator'][i] = 'PP'
    elif corpus_14['Compound_Score'][i] < -0.0516:
        corpus_14['Indicator'][i] = 'Neg'
    else:
        corpus_14['Indicator'][i] = 'NN'
    i +=1
    
i=0
corpus_15['Compound_Score']
while i < len(corpus_15['retweets']):
    if corpus_15['Compound_Score'][i] > 0.0516:
        corpus_15['Indicator'][i] = 'PP'
    elif corpus_15['Compound_Score'][i] < -0.0516:
        corpus_15['Indicator'][i] = 'Neg'
    else:
        corpus_15['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_16['Compound_Score']
while i < len(corpus_16['retweets']):
    if corpus_16['Compound_Score'][i] > 0.0516:
        corpus_16['Indicator'][i] = 'PP'
    elif corpus_16['Compound_Score'][i] < -0.0516:
        corpus_16['Indicator'][i] = 'Neg'
    else:
        corpus_16['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_17['Compound_Score']
while i < len(corpus_17['retweets']):
    if corpus_17['Compound_Score'][i] > 0.0516:
        corpus_17['Indicator'][i] = 'PP'
    elif corpus_17['Compound_Score'][i] < -0.0516:
        corpus_17['Indicator'][i] = 'Neg'
    else:
        corpus_17['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_18['Compound_Score']
while i < len(corpus_18['retweets']):
    if corpus_18['Compound_Score'][i] > 0.0516:
        corpus_18['Indicator'][i] = 'PP'
    elif corpus_18['Compound_Score'][i] < -0.0516:
        corpus_18['Indicator'][i] = 'Neg'
    else:
        corpus_18['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_19['Compound_Score']
while i < len(corpus_19['retweets']):
    if corpus_19['Compound_Score'][i] > 0.0516:
        corpus_19['Indicator'][i] = 'PP'
    elif corpus_19['Compound_Score'][i] < -0.0516:
        corpus_19['Indicator'][i] = 'Neg'
    else:
        corpus_19['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_20['Compound_Score']
while i < len(corpus_20['retweets']):
    if corpus_20['Compound_Score'][i] > 0.0516:
        corpus_20['Indicator'][i] = 'PP'
    elif corpus_20['Compound_Score'][i] < -0.0516:
        corpus_20['Indicator'][i] = 'Neg'
    else:
        corpus_20['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_21['Compound_Score']
while i < len(corpus_21['retweets']):
    if corpus_21['Compound_Score'][i] > 0.0516:
        corpus_21['Indicator'][i] = 'PP'
    elif corpus_21['Compound_Score'][i] < -0.0516:
        corpus_21['Indicator'][i] = 'Neg'
    else:
        corpus_21['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_22['Compound_Score']
while i < len(corpus_22['retweets']):
    if corpus_22['Compound_Score'][i] > 0.0516:
        corpus_22['Indicator'][i] = 'PP'
    elif corpus_22['Compound_Score'][i] < -0.0516:
        corpus_22['Indicator'][i] = 'Neg'
    else:
        corpus_22['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_23['Compound_Score']
while i < len(corpus_23['retweets']):
    if corpus_23['Compound_Score'][i] > 0.0516:
        corpus_23['Indicator'][i] = 'PP'
    elif corpus_23['Compound_Score'][i] < -0.0516:
        corpus_23['Indicator'][i] = 'Neg'
    else:
        corpus_23['Indicator'][i] = 'NN'
    i +=1
    
i=0
corpus_24['Compound_Score']
while i < len(corpus_24['retweets']):
    if corpus_24['Compound_Score'][i] > 0.0516:
        corpus_24['Indicator'][i] = 'PP'
    elif corpus_24['Compound_Score'][i] < -0.0516:
        corpus_24['Indicator'][i] = 'Neg'
    else:
        corpus_24['Indicator'][i] = 'NN'
    i +=1
    
i=0
corpus_25['Compound_Score']
while i < len(corpus_25['retweets']):
    if corpus_25['Compound_Score'][i] > 0.0516:
        corpus_25['Indicator'][i] = 'PP'
    elif corpus_25['Compound_Score'][i] < -0.0516:
        corpus_25['Indicator'][i] = 'Neg'
    else:
        corpus_25['Indicator'][i] = 'NN'
    i +=1

i=0
corpus_26['Compound_Score']
while i < len(corpus_26['retweets']):
    if corpus_26['Compound_Score'][i] > 0.0516:
        corpus_26['Indicator'][i] = 'PP'
    elif corpus_26['Compound_Score'][i] < -0.0516:
        corpus_26['Indicator'][i] = 'Neg'
    else:
        corpus_26['Indicator'][i] = 'NN'
    i +=1

corpus_13.to_csv('corpus_13.csv', index = False, encoding = 'utf-8')
corpus_14.to_csv('corpus_14.csv', index = False, encoding = 'utf-8')
corpus_15.to_csv('corpus_15.csv', index = False, encoding = 'utf-8')
corpus_16.to_csv('corpus_16.csv', index = False, encoding = 'utf-8')
corpus_17.to_csv('corpus_17.csv', index = False, encoding = 'utf-8')
corpus_18.to_csv('corpus_18.csv', index = False, encoding = 'utf-8')
corpus_19.to_csv('corpus_19.csv', index = False, encoding = 'utf-8')
corpus_20.to_csv('corpus_20.csv', index = False, encoding = 'utf-8')
corpus_21.to_csv('corpus_21.csv', index = False, encoding = 'utf-8')
corpus_22.to_csv('corpus_22.csv', index = False, encoding = 'utf-8')
corpus_23.to_csv('corpus_23.csv', index = False, encoding = 'utf-8')
corpus_24.to_csv('corpus_24.csv', index = False, encoding = 'utf-8')
corpus_25.to_csv('corpus_25.csv', index = False, encoding = 'utf-8')
corpus_26.to_csv('corpus_26.csv', index = False, encoding = 'utf-8')


corpus_13 = pd.read_csv('corpus_13.csv')
corpus_14 = pd.read_csv('corpus_14.csv')
corpus_15 = pd.read_csv('corpus_15.csv')
corpus_16 = pd.read_csv('corpus_16.csv')
corpus_17 = pd.read_csv('corpus_17.csv')
corpus_18 = pd.read_csv('corpus_18.csv')
corpus_19 = pd.read_csv('corpus_19.csv')
corpus_20 = pd.read_csv('corpus_20.csv')
corpus_21 = pd.read_csv('corpus_21.csv')
corpus_22 = pd.read_csv('corpus_22.csv')
corpus_23 = pd.read_csv('corpus_23.csv')
corpus_24 = pd.read_csv('corpus_24.csv')


###Average Sentiment Score
sen_13 = np.mean(corpus_13['Compound_Score'])
sen_14 = np.mean(corpus_14['Compound_Score'])
sen_15 = np.mean(corpus_15['Compound_Score'])
sen_16 = np.mean(corpus_16['Compound_Score'])
sen_17 = np.mean(corpus_17['Compound_Score'])
sen_18 = np.mean(corpus_18['Compound_Score'])
sen_19 = np.mean(corpus_19['Compound_Score'])
sen_20 = np.mean(corpus_20['Compound_Score'])
sen_21 = np.mean(corpus_21['Compound_Score'])
sen_22 = np.mean(corpus_22['Compound_Score'])
sen_23 = np.mean(corpus_23['Compound_Score'])
sen_24 = np.mean(corpus_24['Compound_Score'])
sen_25 = np.mean(corpus_25['Compound_Score'])
sen_26 = np.mean(corpus_26['Compound_Score'])

aver_sent = [sen_13, sen_14, sen_15, sen_16, sen_17, sen_18, sen_19, sen_20,
             sen_21, sen_22, sen_23, sen_24]#, sen_25, sen_26]
Aver_sent = pd.DataFrame({'col':aver_sent})

#Happy Death Day
rank = [1,1,1,2,2,2,2,3,3,3,4,4]
Rank = pd.DataFrame({'col':rank})

#Deadpool
rank = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Rank = pd.DataFrame({'col':rank})

###Google Trends
#Happy Death Day
corpus_13['GT']= 77
corpus_14['GT']= 100
corpus_15['GT']= 99
corpus_16['GT']= 77
corpus_17['GT']= 59
corpus_18['GT']= 51
corpus_19['GT']= 45
corpus_20['GT']= 47
corpus_21['GT']= 62
corpus_22['GT']= 60
corpus_23['GT']= 39
corpus_24['GT']= 30
corpus_25['GT']= 28
corpus_26['GT']= 25

GT = [30, 28, 25, 27, 32, 44, 39, 22, 21, 18, 20, 23]
len(GT)
Google_Trend = pd.DataFrame({'col':GT})

#Deadpool
GT = [77, 100, 99, 77, 59, 51, 45, 47, 62, 60, 39, 30]#, 28, 25]
len(GT)
Google_Trend = pd.DataFrame({'col':GT})

#Happy Death Day
Daily_gross = [11659375, 9362760, 5016890, 1366905, 1727445, 1059510, 1116480, 2989520,
               4095415, 2278480, 644240, 883010, 565805]

Daily_gross_1 = [9362760, 5016890, 1366905, 1727445, 1059510, 1116480, 2989520,
               4095415, 2278480, 644240, 883010, 565805]

Daily_gross_2 = [11659375, 9362760, 5016890, 1366905, 1727445, 1059510, 1116480, 2989520,
               4095415, 2278480, 644240, 883010]

#Deadpool
Daily_gross_1 = [42508025, 42591022, 19759214, 11559606, 8617589, 8023839, 16218008, 24291774, 15960385, 4465513, 5158806, 3795778, 
                 3853861, 8879279]

Daily_gross_2 = [47335592, 42508025, 42591022, 19759214, 11559606, 8617589, 8023839, 16218008, 24291774, 15960385, 4465513, 5158806]#, 3795778, 
                 #3853861]

fav = [fav_13, fav_14, fav_15, fav_16, fav_17, fav_18, fav_19, fav_20, fav_21, fav_22, 
       fav_23, fav_24]#, fav_25, fav_26 ]
Fav = pd.DataFrame({'col':fav})

retweett = [retweets_13, retweets_14, retweets_15, retweets_16, retweets_17, retweets_18, retweets_19,
            retweets_20, retweets_21, retweets_22, retweets_23, retweets_24]#, retweets_25, retweets_26]
Retweett = pd.DataFrame({'col':retweett})


#Happy Death Day
daily_theatre = [3149, 3149, 3149, 3149, 3149, 3149, 3149, 3298, 3298, 3298, 3298, 3298]
Daily_theatre = pd.DataFrame({'col':daily_theatre})

#Deadpool
daily_theatre = [3558, 3558, 3558, 3558, 3558, 3558, 3558, 3722, 3722, 3722, 3722, 3722]#, 3722, 3722]
Daily_theatre = pd.DataFrame({'col':daily_theatre})


# Create linear regression object
#Separate
"""
#This is a R^2 calculation model that I decide not to use



regr.fit(Aver_sent, Daily_gross_1)
gross_pred = regr.predict(Aver_sent)
print('Variance score: %.2f' % r2_score(Daily_gross_1, gross_pred))

regr.fit(Rank, Daily_gross)
gross_pred = regr.predict(Rank)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

regr.fit(Fav, Daily_gross)
gross_pred = regr.predict(Fav)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

regr.fit(Retweett, Daily_gross)
gross_pred = regr.predict(Retweett)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

regr.fit(Daily_theatre, Daily_gross)
gross_pred = regr.predict(Daily_theatre)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))
"""
regr = linear_model.LinearRegression()

model = sm.OLS(Aver_sent, Daily_gross_1)
results = model.fit()
print(results.summary())

model = sm.OLS(Aver_sent, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Fav, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Retweett, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Daily_theatre, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(GT, Daily_gross_2)
results = model.fit()
print(results.summary())

###############################################################################

regr.fit(Aver_sent, Daily_gross_2)
gross_pred = regr.predict(Aver_sent)
print('Variance score: %.2f' % r2_score(Daily_gross_2, gross_pred))

regr.fit(Rank, Daily_gross)
gross_pred = regr.predict(Rank)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

regr.fit(Fav, Daily_gross)
gross_pred = regr.predict(Fav)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

regr.fit(Retweett, Daily_gross)
gross_pred = regr.predict(Retweett)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

regr.fit(Daily_theatre, Daily_gross)
gross_pred = regr.predict(Daily_theatre)
print('Variance score: %.2f' % r2_score(Daily_gross, gross_pred))

model = sm.OLS(Daily_gross_2, Aver_sent)
model = sm.OLS(Aver_sent, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Aver_sent, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Fav, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Retweett, Daily_gross_2)
results = model.fit()
print(results.summary())

model = sm.OLS(Daily_theatre, Daily_gross_2)
results = model.fit()
print(results.summary())


#All together
Use = pd.concat([Aver_sent, Rank, Fav, Retweett, Daily_theatre, Google_Trend], axis=1, 
                join_axes=[Aver_sent.index])

regr.fit(Use, Daily_gross_2)
gross_pred = regr.predict(Use)
print('Variance score: %.2f' % r2_score(Daily_gross_2, gross_pred))



MLPClassifier(solver='lbfgs', hidden_layer_sizes=(15,), random_state=1,alpha=1e-5)

###PIPELINED RANDOM FOREST FEATURE
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
#from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC
#from sklearn.model_selection import GridSearchCV

movie_train = Use[0:11]; movie_test = Use[11:12]
DG_train = Daily_gross_2[0:11]; DG_test = Daily_gross_2[11:12]

movie_train = Use[0:13]; movie_test = Use[13:14]
DG_train = Daily_gross_2[0:13]; DG_test = Daily_gross_2[13:14]

text_clfPipe = Pipeline([
                      ('clf-rf', RandomForestClassifier(max_depth=2, random_state=0)),
])
text_clf = text_clfPipe.fit(movie_train, DG_train)
predicted = text_clf.predict(movie_test)
print [DG_test, predicted]

print('Variance score: %.2f' % r2_score(Daily_gross, predicted))
acc = np.mean(predicted == twenty_test.target)

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-3, n_iter=5, random_state=42)),
])
text_clf = text_clf.fit(movie_train, DG_train)
predicted = text_clf.predict(movie_test)
print [DG_test, predicted]

parameters = {'clf__alpha': (1e-2, 1e-3),
            }

gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(Use, Daily_gross)

print gs_clf.best_score_
optParams = gs_clf.best_params_

