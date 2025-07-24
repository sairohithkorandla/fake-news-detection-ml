from FakeStatements.users.algorithm import FeatureSelection
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
nb_pipeline = Pipeline([
        ('NBCV', FeatureSelection.countV),
        ('nb_clf',MultinomialNB())])
print(type(nb_pipeline))

score = build_confusion_matrix(nb_pipeline)
print('Score is ',score)

#logR_pipeline_ngram = Pipeline([('LogR_tfidf',FeatureSelection.tfidf_ngram),('LogR_clf',LogisticRegression(penalty="l2",C=1))])
#show_most_informative_features(logR_pipeline_ngram,vect='LogR_tfidf',clf='LogR_clf')