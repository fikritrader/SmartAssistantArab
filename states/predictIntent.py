from keras.layers import Dense, Dropout, Embedding, LSTM, GlobalMaxPooling1D, SpatialDropout1D
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
import pickle,json
import os

currentPath = os.path.dirname(os.path.dirname(__file__))
modelDataPath = os.path.join(currentPath,"misc/intentModel")
modelUtilityDataPath = os.path.join(currentPath ,"misc/utilityModel")

params = json.load(open(os.path.join(modelDataPath ,'parameters.json'),'r'))
maxWords=params['maxWords']
maxPhraseLen=params['maxLen']


def createModel(output,maxWords):
    model_lstm = Sequential()
    model_lstm.add(Embedding(input_dim = maxWords, output_dim = 256, input_length = maxPhraseLen))
    model_lstm.add(SpatialDropout1D(0.3))
    model_lstm.add(LSTM(256, dropout = 0.3, recurrent_dropout = 0.3))
    model_lstm.add(Dense(256, activation = 'relu'))
    model_lstm.add(Dropout(0.3))
    model_lstm.add(Dense(output, activation = 'softmax'))
    model_lstm.compile(
        loss='categorical_crossentropy',
        optimizer='Adam',
        metrics=['accuracy']
    )
    return model_lstm

#these two functino are for predicting the intent on the main tree

def predict(s):
    path = os.path.join(modelDataPath,'tokenizer.p')
    tokenizer = pickle.load(open(path,'rb'))
    model = createModel(8,maxWords)
    path = os.path.join(modelDataPath,'intent.h5')
    model = load_model(path)
    inputD = tokenizer.texts_to_sequences([s])
    inputD = pad_sequences(inputD, maxlen = maxPhraseLen)
    prediction = model.predict(inputD)
    return prediction.argmax()

#this function are for predicting the intent on the utility state
def predictUtility(s):
    modelUtilityDataPath = os.path.join(currentPath,"misc/utilityModel")
    paramsUtil = json.load(open(os.path.join(modelUtilityDataPath,'parameters.json'),'r'))
    maxWordsUtil=paramsUtil['maxWords']
    maxPhraseLenUtil=paramsUtil['maxLen']

    path = os.path.join(modelUtilityDataPath,'tokenizer.p')
    tokenizer = pickle.load(open(path,'rb'))
    model = createModel(4,maxWordsUtil)
    path = os.path.join(modelUtilityDataPath,'intent.h5')
    model = load_model(path)
    inputD = tokenizer.texts_to_sequences([s])
    inputD = pad_sequences(inputD, maxlen = maxPhraseLenUtil)
    prediction = model.predict(inputD)
    return prediction.argmax()
    
#this function are for predicting the wanted story
def predictStory(s):
    modelStoryDataPath = os.path.join(currentPath,"misc/storyModel")
    paramsStory = json.load(open(os.path.join(modelStoryDataPath,'parameters.json'),'r'))
    maxWordsUtil=paramsStory['maxWords']
    maxPhraseLenStory=paramsStory['maxLen']

    path = os.path.join(modelStoryDataPath,'tokenizer.p')
    tokenizer = pickle.load(open(path,'rb'))
    model = createModel(6,maxWordsUtil)
    path = os.path.join(modelStoryDataPath,'intent.h5')
    model = load_model(path)
    inputD = tokenizer.texts_to_sequences([s])
    inputD = pad_sequences(inputD, maxlen = maxPhraseLenStory)
    prediction = model.predict(inputD)
    return prediction.argmax()