# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:45:40 2017

@author: NishitP
"""
from django.conf import settings
import pickle

#doc_new = ['obama is running for president in 2016']

#var = input("Please enter the news text you want to verify: ")
#print("You entered: " + str(var))


#function to run for prediction
def detecting_fake_news(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open(settings.MEDIA_ROOT + "\\" +'final_model.sav', 'rb'))
    #print('Thoda katti Kojaye ',type(load_model))
    prediction = load_model.predict([var])
    #print(prediction)
    prob = load_model.predict_proba([var])
    dict = {'label':prediction[0],'score':prob[0][1]}
    return dict


#if __name__ == '__main__':
    #detecting_fake_news(var)