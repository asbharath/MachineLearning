from FrenchEnglish import *

def main():
    obj = FrenchEnglish()
    ml = MachineLearning()
    filename = 'fra.txt'
    clean_pickle = 'french-english.pkl'
    doc = obj.load_data(filename)
    pairs = obj.convert_pairs(doc)
    clean_pairs = obj.clean_data(pairs)
    obj.save_clean_data(clean_pairs, clean_pickle)

    # for i in range(10):
    #     print('%s ==> %s' % (clean_pairs[i, 0], clean_pairs[i, 1]))

    raw_data = obj.load_clean_dataset(clean_pickle)
    obj.shuffle(raw_data)

    train,test = ml.train_split(raw_data)

    obj.save_clean_data(train,'train-french-english.pkl')
    obj.save_clean_data(test, 'test-french-english.pkl')



if __name__ == "__main__":
    main()





