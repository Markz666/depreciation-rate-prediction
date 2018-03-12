# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 23:34:22 2017

@author: zmx
"""
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
def sentiment_analysis(brand):
    comments = []
    filename = brand + "_comment.csv"
    with open(filename, 'r') as inf:
        spamreader = csv.reader(inf)
        for row in spamreader:
            comments.append(str(row))
    print("Sentiment Analysis for " + brand + ":")
    for comment in comments:
#        print(comment)
        ss = sid.polarity_scores(comment)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]))q      

if __name__ == "__main__":
    filenames = ["BMW", "Ford", "Honda", "Lexus", "Mazda", "Toyota", "Audi", "Chevrolet", "Jeep", "Mercedes-Benz", "Dodge"]
#    filenames = ["Dodge", "Nissan"]    
    for filename in filenames:
        sentiment_analysis(filename)
