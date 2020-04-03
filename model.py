import warnings
warnings.filterwarnings('ignore')
import scipy.io as sc
import numpy as np
import random
import sys
from sklearn import preprocessing
from keras import backend as K
from keras.models import load_model
from xgboost import XGBClassifier
import pickle

##Allowing GPU memory to be used
from keras.backend.tensorflow_backend import set_session
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.8
session = tf.Session(config=config)
set_session(session)

#loading models
cnnmodel = load_model('cnn.hdf5')
rnnmodel = load_model('rnn.hdf5')
fcc = load_model('fcc.hdf5')
xgbmodel = pickle.load(open("xgb", "rb"))

get_cnn_output = K.function([cnnmodel.layers[0].input],[cnnmodel.layers[5].output])
get_rnn_output = K.function([rnnmodel.layers[0].input],[rnnmodel.layers[0].output])
get_fcc_output = K.function([fcc.layers[0].input],[fcc.layers[0].output])


def predict(sequence):

    cnn_out = []
    train_fea_re = sequence.reshape(1, 64, 1).astype('float32')
    out = get_cnn_output([train_fea_re])
    cnn_out.append(out[0][0])

    rnn_out = []
    train_fea_re = sequence.reshape([1,1,64]).astype('float32')
    out = get_rnn_output([train_fea_re])
    rnn_out.append(out[0][0])

    fcc_out = []
    train = []
    train.extend(cnn_out[0])
    train.extend(rnn_out[0])
    train = np.asarray(train)
    train_fea_re = train.reshape(1,300).astype('float32')
    out = get_fcc_output([train_fea_re])
    fcc_out.append(out[0][0])

    train = np.asarray(fcc_out[0])
    train_fea_re = train.reshape(1,30).astype('float32')
    out = xgbmodel.predict(train_fea_re)

    if out == 3:
        xgb_out = '/'
    else:
        xgb_out = (str)(out[0]-1)

    return(xgb_out)
