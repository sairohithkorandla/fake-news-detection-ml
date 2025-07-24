from FakeStatements.users.algorithm.classifier import  show_most_informative_features
from FakeStatements.users.algorithm import FeatureSelection
from sklearn.linear_model import  LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

nb_pipeline = Pipeline([
        ('NBCV', FeatureSelection.countV),
        ('nb_clf',MultinomialNB())])

build_confusion_matrix(nb_pipeline)

logR_pipeline_ngram = Pipeline([
        ('LogR_tfidf', FeatureSelection.tfidf_ngram),
        ('LogR_clf',LogisticRegression(penalty="l2",C=1))
        ])
show_most_informative_features(logR_pipeline_ngram,vect='LogR_tfidf',clf='LogR_clf')