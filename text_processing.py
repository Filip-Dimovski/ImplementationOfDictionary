import nltk
import random
from nltk.tokenize import word_tokenize
#from sklearn import svm
from nltk.classify.scikitlearn import SklearnClassifier
#from sklearn.naive_bayes import MultinomialNB

def separate_by_words(file_name):
    file=open(file_name)
    all_words=[]
    for w in word_tokenize(file.read()):
        if w not in stop_words:
            all_words.append(w.lower())
    file.close()
    return all_words

def most_freq_words(file):
    freq_words=[]
    freq_words=separate_by_words(file)
    freq_words=nltk.FreqDist(freq_words)
    return freq_words

def most_freq_15_words(file,keyword):
    all_words=most_freq_words(file)
    print(all_words.most_common(15))
    print('Count of the word '+keyword+' : ' +str(all_words[keyword]))

def find_features(file_name):
    words=set(separate_by_words(file_name))
    word_features=list(most_freq_words(file_name).keys())[:3000]
    features=[]
    for w in word_features:
        features[w]=(w in words)
    return features


stop_words=[',','.','-',':','\'','во','на','а','некој','некои','некоја','секогаш','овде','овие','тука','таму','секогаш','никогаш','кој','кога','каде','ќе','ви','што','да','овие','оние','и','се','со','го','е','-','не','од','за','по','неговиот','неговата','му','дека','кои']
features={}
featureset=[]
print('Most frequent words in music:')
most_freq_15_words("antenna5/content.txt",'британски')

for w in most_freq_words("antenna5/content.txt"):
    features[w]='music'
featureset=[features,'neg']



print('Most frequent words in football:')
most_freq_15_words("24fudbal/content.txt",'топка')

features={}
for w in most_freq_words("24fudbal/content.txt"):
    features[w]='football'
featureset=[features,'pos']

print('Most frequent words in astronomy:')
most_freq_15_words("astronomija/content.txt",'планета')

features={}
for w in most_freq_words("astronomija/content.txt"):
    features[w]='astronomy'
featureset=[features,'neg']
            
print('Most frequent words in sport:')
most_freq_15_words("ekipa/content.txt",'топка')

features={}
for w in most_freq_words("ekipa/content.txt"):
    features[w]='sport'
featureset=[features,'pos']

print('Most frequent words in fashion:')
most_freq_15_words("fashionel/content.txt",'мода')

features={}
for w in most_freq_words("fashionel/content.txt"):
    features[w]= 'fashion'
featureset=[features,'neg']

print('Most frequent words in lifestyle:')
most_freq_15_words("kafepauza/content.txt",'живот')

features={}
for w in most_freq_words("kafepauza/content.txt"):
    features[w]='lifestyle'
featureset=[features,'neg']

print('Most frequent words in technology:')
most_freq_15_words("smartportal/content.txt",'дисплеј')

features={}
for w in most_freq_words("smartportal/content.txt"):
    features[w]='technology'
featureset=[features,'neg']

#for field, possible_values in features.items():
#    print(field, possible_values)

#training_set=featureset[:190]
#testing_set=featureset[190:]

#print(len(featureset[1]))
#print(training_set)

#classifier=nltk.NaiveBayesClassifier.train(featureset)
#print('Naive Bayes Algo accuracy percent: ',(nltk.classify.accuracy(classifier,testing_set))*100)
#classifier.show_most_informative_features(15) 
