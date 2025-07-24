from users.algorithm import DataPrep
from users.algorithm import  FeatureSelection
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
# from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import KFold
from warnings import simplefilter

# string to test
doc_new = ['obama is running for president in 2016']

# the feature selection has been done in FeatureSelection.py module. here we will create models using those features for prediction

# first we will use bag of words techniques

# building classifier using naive bayes
nb_pipeline = Pipeline([
    ('NBCV', FeatureSelection.countV),
    ('nb_clf', MultinomialNB())])

nb_pipeline.fit(DataPrep.train_news['Statement'], DataPrep.train_news['Label'])
predicted_nb = nb_pipeline.predict(DataPrep.test_news['Statement'])
np.mean(predicted_nb == DataPrep.test_news['Label'])

# building classifier using logistic regression
logR_pipeline = Pipeline([('LogRCV', FeatureSelection.countV), ('LogR_clf', LogisticRegression())])

logR_pipeline.fit(DataPrep.train_news['Statement'], DataPrep.train_news['Label'])
predicted_LogR = logR_pipeline.predict(DataPrep.test_news['Statement'])
np.mean(predicted_LogR == DataPrep.test_news['Label'])


# User defined functon for K-Fold cross validatoin
def build_confusion_matrix(classifier):
    # print('Total statements classified:', len(DataPrep.train_news))
    simplefilter(action='ignore', category=FutureWarning)
    k_fold = KFold(len(DataPrep.train_news), False)
    scores = []
    confusion = np.array([[0, 0], [0, 0]])

    for train_ind, test_ind in k_fold.split(DataPrep.train_news['Statement']):
        train_text = DataPrep.train_news.iloc[train_ind]['Statement']
        train_y = DataPrep.train_news.iloc[train_ind]['Label']

        test_text = DataPrep.train_news.iloc[test_ind]['Statement']
        test_y = DataPrep.train_news.iloc[test_ind]['Label']

        classifier.fit(train_text, train_y)
        predictions = classifier.predict(test_text)

        confusion += confusion_matrix(test_y, predictions)
        score = f1_score(test_y, predictions)
        scores.append(score)

    return (sum(scores) / len(scores)
            )






nb_pipeline_ngram = Pipeline([('nb_tfidf', FeatureSelection.tfidf_ngram), ('nb_clf', MultinomialNB())])
nb_pipeline_ngram.fit(DataPrep.train_news['Statement'], DataPrep.train_news['Label'])
predicted_nb_ngram = nb_pipeline_ngram.predict(DataPrep.test_news['Statement'])
np.mean(predicted_nb_ngram == DataPrep.test_news['Label'])

# logistic regression classifier
logR_pipeline_ngram = Pipeline([('LogR_tfidf', FeatureSelection.tfidf_ngram), ('LogR_clf', LogisticRegression(penalty="l2", C=1))])

logR_pipeline_ngram.fit(DataPrep.train_news['Statement'], DataPrep.train_news['Label'])
predicted_LogR_ngram = logR_pipeline_ngram.predict(DataPrep.test_news['Statement'])
np.mean(predicted_LogR_ngram == DataPrep.test_news['Label'])




def runAlgorithm():

    logRClas = build_confusion_matrix(logR_pipeline)


    dict = {
        'LogicRegressionClassification': round(logRClas, 2),

    }
    return dict;


#print(dict)
