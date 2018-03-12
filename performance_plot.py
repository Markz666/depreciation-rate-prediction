# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:12:13 2017

@author: zmx
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_generate(scores, title_text):
    NUMBER_OF_GROUPS = 10
    index = np.arange(NUMBER_OF_GROUPS)
    bar_width = 0.6
    opacity = 0.7
    results = plt.bar(index, scores, bar_width, alpha = opacity)
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.title(title_text)
    plt.xticks(index, ("SVM","CART","RFC","KNN","RFR","GNB","BNB","LG","MNB","LR"))
    #plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    title1="Performance of different models with all parameters"
    scores1 = (0.942,0.942,0.942,0.936,0.912,0.245,0.228,0.228,0.133,0.0197)
    plot_generate(scores1,title1)
    title2 = "Performace of different models with non-sentiment analysis"
    scores2 = (0.942,0.942,0.942,0.935,0.912,0.2346,0.2445,0.228,0.111,0.0048)
    plot_generate(scores2,title2)