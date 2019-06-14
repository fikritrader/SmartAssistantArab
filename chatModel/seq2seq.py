import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, CuDNNLSTM, Input, Embedding, TimeDistributed, Flatten, Dropout
from keras.callbacks import ModelCheckpoint

num_samples = 10000  # Number of samples to train on.
# Path to the data txt file on disk.
data_path = 'chatModel/data/dataSetCleaned.txt'

# Vectorize the data.
input_texts = []
target_texts = []
input_characters = set()
target_characters = set()
with open(data_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
lineIndex=0
for line in lines[: min(num_samples, len(lines) - 1)]:
    print('line : ',lineIndex)
    lineIndex+=1
    input_text=""
    target_text,input_text = line.split('$splt$')
    # We use "tab" as the "start sequence" character
    # for the targets, and "\n" as "end sequence" character.
    target_text = '\t' + target_text + '\n'
    input_texts.append(input_text)
    target_texts.append(target_text)
    for char in input_text.split(' '):
        if char not in input_characters:
            input_characters.add(char)
    for char in target_text.split(' '):
        if char not in target_characters:
            target_characters.add(char)

input_characters = sorted(list(input_characters))
target_characters = sorted(list(target_characters))
num_encoder_tokens = len(input_characters)
num_decoder_tokens = len(target_characters)
max_encoder_seq_length = max([len(txt) for txt in input_texts])
max_decoder_seq_length = max([len(txt) for txt in target_texts])

print('Number of samples:', len(input_texts))
print('Number of unique input tokens:', num_encoder_tokens)
print('Number of unique output tokens:', num_decoder_tokens)
print('Max sequence length for inputs:', max_encoder_seq_length)
print('Max sequence length for outputs:', max_decoder_seq_length)



input_token_index = dict(
    [(char, i) for i, char in enumerate(input_characters)])
target_token_index = dict(
    [(char, i) for i, char in enumerate(target_characters)])



encoder_input_data = np.zeros(
    (len(input_texts), num_encoder_tokens),
    dtype='int8')
decoder_input_data = np.zeros(
    (len(input_texts), num_decoder_tokens),
    dtype='int8')
decoder_target_data = np.zeros(
    (len(input_texts), num_decoder_tokens),
    dtype='int8')

for i, (input_text, target_text) in enumerate(zip(input_texts, target_texts)):
    for t, char in enumerate(input_text.split(' ')):
        encoder_input_data[i, input_token_index[char]] = 1
    for t, char in enumerate(target_text.split(' ')):
        decoder_input_data[i, target_token_index[char]] = 1
        if t > 0:
            # decoder_target_data will be ahead by one timestep
            # and will not include the start character.
            decoder_target_data[i, target_token_index[char]] = 1


# Defining some constants: 
vec_len       = 300   # Length of the vector that we willl get from the embedding layer
latent_dim    = 1024  # Hidden layers dimension 
dropout_rate  = 0.2   # Rate of the dropout layers
batch_size    = 64    # Batch size
epochs        = 30    # Number of epochs

# Define an input sequence and process it.
# Input layer of the encoder :
encoder_input = Input(shape=(None,))

# Hidden layers of the encoder :
encoder_embedding = Embedding(input_dim = num_encoder_tokens, output_dim = vec_len)(encoder_input)
encoder_dropout   = (TimeDistributed(Dropout(rate = dropout_rate)))(encoder_embedding)
encoder_LSTM      = LSTM(latent_dim, return_sequences=True)(encoder_dropout)

# Output layer of the encoder :
encoder_LSTM2_layer = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder_LSTM2_layer(encoder_LSTM)

# We discard `encoder_outputs` and only keep the states.
encoder_states = [state_h, state_c]



# Set up the decoder, using `encoder_states` as initial state.
# Input layer of the decoder :
decoder_input = Input(shape=(None,))

# Hidden layers of the decoder :
decoder_embedding_layer = Embedding(input_dim = num_decoder_tokens, output_dim = vec_len)
decoder_embedding = decoder_embedding_layer(decoder_input)

decoder_dropout_layer = (TimeDistributed(Dropout(rate = dropout_rate)))
decoder_dropout = decoder_dropout_layer(decoder_embedding)

decoder_LSTM_layer = LSTM(latent_dim, return_sequences=True)
decoder_LSTM = decoder_LSTM_layer(decoder_dropout, initial_state = encoder_states)

decoder_LSTM_2_layer = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_LSTM_2,_,_ = decoder_LSTM_2_layer(decoder_LSTM)

# Output layer of the decoder :
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_LSTM_2)

# Define the model that will turn
# `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
model = Model([encoder_input, decoder_input], decoder_outputs)

model.summary()

# Define a checkpoint callback :
checkpoint_name = 'Weights-{epoch:03d}--{val_loss:.5f}.hdf5' 
checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
callbacks_list = [checkpoint]

print('Number of samples:', len(input_texts))
print('Number of unique input tokens:', num_encoder_tokens)
print('Number of unique output tokens:', num_decoder_tokens)
print('Max sequence length for inputs:', max_encoder_seq_length)
print('Max sequence length for outputs:', max_decoder_seq_length)
decoder_target_data=decoder_target_data.reshape(len(input_texts),1,num_decoder_tokens)
# Run training
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit([encoder_input_data,decoder_input_data],decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.08,
          callbacks = callbacks_list)
model.save('s2s.h5')