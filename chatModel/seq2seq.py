from keras.models import Model
from keras.layers import Input, LSTM, Dense,CuDNNLSTM
import numpy as np


batch_size = 64  # Batch size for training.
epochs = 100  # Number of epochs to train for.
latent_dim = 256  # Latent dimensionality of the encoding space.
num_samples = 100000  # Number of samples to train on.
# Path to the data txt file on disk.
data_path = 'chatModel/data/cleanFile.txt'

# Vectorize the data.
input_texts = []
target_texts = []
input_characters = set()
target_characters = set()

characters_fixed =['\t', ' ', '؟', 'ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي', 'ٱ', 'چ', 'ڤ', 'ک', 'گ', 'ۃ', 'ۆ', 'ی', 'ﺀ', 'ﺃ', 'ﺄ', 'ﺉ', 'ﺋ', 'ﺍ', 'ﺎ', 'ﺏ', 'ﺑ', 'ﺒ', 'ﺓ', 'ﺔ', 'ﺕ', 'ﺖ', 'ﺗ', 'ﺘ', 'ﺛ', 'ﺟ', 'ﺠ', 'ﺣ', 'ﺤ', 'ﺧ', 'ﺨ', 'ﺪ', 'ﺬ', 'ﺭ', 'ﺮ', 'ﺰ', 'ﺲ', 'ﺳ', 'ﺴ', 'ﺶ', 'ﺸ', 'ﺻ', 'ﺼ', 'ﺿ', 'ﻀ', 'ﻄ', 'ﻈ', 'ﻊ', 'ﻋ', 'ﻌ', 'ﻐ', 'ﻓ', 'ﻔ', 'ﻖ', 'ﻗ', 'ﻘ', 'ﻙ', 'ﻚ', 'ﻛ', 'ﻜ', 'ﻞ', 'ﻟ', 'ﻠ', 'ﻡ', 'ﻢ', 'ﻣ', 'ﻤ', 'ﻥ', 'ﻦ', 'ﻧ', 'ﻨ', 'ﻩ', 'ﻪ', 'ﻫ', 'ﻬ', 'ﻭ', 'ﻮ', 'ﻯ', 'ﻰ', 'ﻲ', 'ﻳ', 'ﻴ', 'ﻵ', 'ﻷ', 'ﻹ', 'ﻻ', 'ﻼ']
with open(data_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
lineIndex=0
for line in lines[: min(num_samples, len(lines) - 1)]:
    print('line : ',lineIndex)
    lineIndex+=1
    input_text=""
    input_text,target_text = line.split('$splt$')
    # We use "tab" as the "start sequence" character
    # for the targets, and "\n" as "end sequence" character.
    target_text = '\t' + target_text + '\n'
    input_texts.append(input_text)
    target_texts.append(target_text)
    for char in input_text:
        if char not in input_characters:
            input_characters.add(char)
    for char in target_text:
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
    [(char, i) for i, char in enumerate(characters_fixed)])
target_token_index = dict(
    [(char, i) for i, char in enumerate(characters_fixed)])

encoder_input_data = np.zeros(
    (len(input_texts), max_encoder_seq_length, num_encoder_tokens),
    dtype='int8')
decoder_input_data = np.zeros(
    (len(input_texts), max_decoder_seq_length, num_decoder_tokens),
    dtype='int8')
decoder_target_data = np.zeros(
    (len(input_texts), max_decoder_seq_length, num_decoder_tokens),
    dtype='int8')

for i, (input_text, target_text) in enumerate(zip(input_texts, target_texts)):
    for t, char in enumerate(input_text):
        if char in input_token_index.keys():
            encoder_input_data[i, t, input_token_index[char]] = 1
    for t, char in enumerate(target_text):
        # decoder_target_data is ahead of decoder_input_data by one timestep
        if char in target_token_index.keys():
            decoder_input_data[i, t, target_token_index[char]] = 1
            if t > 0:
                # decoder_target_data will be ahead by one timestep
                # and will not include the start character.
                decoder_target_data[i, t - 1, target_token_index[char]] = 1

print(encoder_input_data.shape)
print(decoder_input_data.shape)
print(decoder_target_data.shape)