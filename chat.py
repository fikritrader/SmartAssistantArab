#! /usr/bin/python
# -*- coding: utf-8 -*-

import tensorflow as tf
import tensorlayer as tl
import numpy as np
from tensorlayer.cost import cross_entropy_seq, cross_entropy_seq_with_mask
from tqdm import tqdm
from data.twitter import data
from sklearn.utils import shuffle
from tensorlayer.models.seq2seq import Seq2seq
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from states.commandHelper import toggleState
import os

def initial_setup(data_corpus):
    metadata, idx_q, idx_a = data.load_data(PATH='data/{}/'.format(data_corpus))
    (trainX, trainY), (testX, testY), (validX, validY) = data.split_dataset(idx_q, idx_a)
    trainX = tl.prepro.remove_pad_sequences(trainX.tolist())
    trainY = tl.prepro.remove_pad_sequences(trainY.tolist())
    testX = tl.prepro.remove_pad_sequences(testX.tolist())
    testY = tl.prepro.remove_pad_sequences(testY.tolist())
    validX = tl.prepro.remove_pad_sequences(validX.tolist())
    validY = tl.prepro.remove_pad_sequences(validY.tolist())
    return metadata, trainX, trainY, testX, testY, validX, validY



def inference(seed, top_n,model_,word2idx,idx2word,start_id,unk_id):
    model_.eval()
    seed_id = [word2idx.get(w, unk_id) for w in seed.split(" ")]
    sentence_id = model_(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n = top_n)
    sentence = []
    for w_id in sentence_id[0]:
        w = idx2word[w_id]
        if w == 'end_id':
            break
        sentence = sentence + [w]
    return sentence

def chatEng():
    data_corpus = "twitter"

    #data preprocessing
    metadata, trainX, trainY, testX, testY, validX, validY = initial_setup(data_corpus)

    # Parameters
    src_len = len(trainX)
    tgt_len = len(trainY)

    assert src_len == tgt_len

    batch_size = 32
    n_step = src_len // batch_size
    src_vocab_size = len(metadata['idx2w']) # 8002 (0~8001)
    emb_dim = 1024

    word2idx = metadata['w2idx']   # dict  word 2 index
    idx2word = metadata['idx2w']   # list index 2 word

    unk_id = word2idx['unk']   # 1
    pad_id = word2idx['_']     # 0

    start_id = src_vocab_size  # 8002
    end_id = src_vocab_size + 1  # 8003

    word2idx.update({'start_id': start_id})
    word2idx.update({'end_id': end_id})
    idx2word = idx2word + ['start_id', 'end_id']

    vocabulary_size=8004
    emb_dim = 1024
    decoder_seq_length = 20
    model_ = Seq2seq(
        decoder_seq_length = decoder_seq_length,
        cell_enc=tf.keras.layers.GRUCell,
        cell_dec=tf.keras.layers.GRUCell,
        n_layer=3,
        n_units=256,
        embedding_layer=tl.layers.Embedding(vocabulary_size=vocabulary_size, embedding_size=emb_dim),
        )

    load_weights = tl.files.load_npz(name='chatModel/model/model.npz')
    tl.files.assign_weights(load_weights, model_)
    
    toggleState("talk")
    playsound("audioBase/willSpeakSp.mp3")
    toggleState("idle")
    r=sr.Recognizer()
    indx=0
    while(True):
        with sr.Microphone() as source:
            print('say something')
            audio=r.listen(source)
        try:
            text=r.recognize_google(audio,language='en')
            file=open("misc/debug/dialogueSp.txt","w",encoding="utf_8")
            file.write(text)
            file.close()
        except:
            text="ok"
            pass
        print(text)
        sentence = inference(text, 1,model_,word2idx,idx2word,start_id,unk_id)
        res=' '.join(sentence)
        if len(res)<2:
            res="no idea"

        print('Zoubida : ',sentence)
        tts=gTTS(res,lang="en")
        tts.save('audioBase/chatSp'+str(indx)+'.mp3')
        toggleState("talk")
        playsound('audioBase/chatSp'+str(indx)+'.mp3')
        toggleState("idle")
        indx=indx+1
        
chatEng()