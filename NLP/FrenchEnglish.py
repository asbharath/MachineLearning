# Includes all the import statements
import os,re,string
from unicodedata import normalize
import numpy as np
from pickle import dump
from pickle import load
from sklearn.model_selection import train_test_split

class FrenchEnglish:
    def load_data(self,filename):
        '''
        This function is going load the file fra.txt from the directory E:\\Datasets\\nlp\\fra-eng
        to be converted as generic one
        :return: text string object containing the data.
        '''
        os.chdir('E:\\Datasets\\nlp\\fra-eng')
        file = open(os.path.join(filename),mode='rt',encoding='UTF-8')
        text = file.read()
        file.close()
        return text

    def convert_pairs(self,text):
        lines = text.strip().split('\n')
        pairs = [l.split('\t') for l in lines]
        return pairs


    def clean_data(self,lines):
        cleaned = list()
        re_print = re.compile('[^%s]' % string.printable)
        table = str.maketrans('','',string.punctuation)
        for line in lines:
            cleaned_pairs = list()
            for pair in line:
                pair = normalize('NFD', pair).encode('ascii','ignore')
                pair = pair.decode('utf-8')
                pair = pair.split()
                pair = [w.lower() for w in pair]
                pair = [w.translate(table) for w in pair]
                pair = [re_print.sub('',w) for w in pair]
                pair = [w for w in pair if w.isalpha()]
                cleaned_pairs.append(' '.join(pair))
            cleaned.append(cleaned_pairs)
        return np.array(cleaned)

    def save_clean_data(self,sentences,filename):
        dump(sentences,open(filename,'wb'))
        print('Saved: %s' % filename)

    def load_clean_dataset(self,filename):
        return load(open(filename,'rb'))

    def shuffle(self,filename):
        return np.random.shuffle(filename)


class MachineLearning:
    def train_split(self,filename):
        train,test = train_test_split(filename,test_size=0.2,random_state=46)
        return train,test