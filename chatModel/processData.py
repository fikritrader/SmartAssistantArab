import numpy as np
import pandas as pd
myData=pd.read_csv('dataSets/arabchatDataset.csv', sep=',',header=0,encoding="utf_8")


# read txtfile into a list line by line :
with open('./dataSets/arabchatDataset.csv', 'r', encoding='utf-8-sig') as f:
    text = f.readlines()
    # Define impty lists to store the samples in them:
en_samples = []
de_samples = []

# Define impty sets to store the characters in them:
en_chars = set()
de_chars = set()

for row in myData.values:
    en_ , de_ = row
    for char in de_:
        if char not in de_chars:
            de_chars.add(char)
    for char in en_:
        if char not in en_chars:
            en_chars.add(char)
    en_samples.append(en_)
    de_samples.append(de_)
   
# Add the chars \t and \n to the sets 
de_chars.add('\n')
de_chars.add('\t')

en_chars.add('\n')
en_chars.add('\t')    

# Make the needed dictionaries to convert characters to integers and the opposite : 
de_char_to_int = dict()
de_int_to_char = dict()
en_char_to_int = dict()
en_int_to_char = dict()

for i,char in enumerate(de_chars):
    de_char_to_int[char] = i
    de_int_to_char[i]    = char
    
for i,char in enumerate(en_chars):    
    en_char_to_int[char] = i
    en_int_to_char[i]    = char

# get lengths and sizes :
num_en_chars = len(en_chars)
num_de_chars = len(de_chars)

max_en_chars_per_sample = max([len(sample) for sample in en_samples])
max_de_chars_per_sample = max([len(sample) for sample in de_samples])

num_en_samples = len(en_samples)
num_de_samples = len(de_samples)

print(f'Number of E Samples  \t: {len(de_samples)}')
print(f'Number of D Samples \t: {len(en_samples)}')

print(f'Number of D Chars  \t: {len(de_chars)}')
print(f'Number of E Chars \t: {len(en_chars)}')

print(f'The Longest D Sample has {max_de_chars_per_sample} Chars')
print(f'The Longest E Sample has {max_en_chars_per_sample} Chars')

# initiate numpy arrays to hold the data that our seq2seq model will use:
encoder_input_data = np.zeros((num_en_samples,
                               max_en_chars_per_sample,
                               num_en_chars))

decoder_input_data = np.zeros((num_de_samples,
                               max_de_chars_per_sample,
                               num_de_chars))

target_data = np.zeros((num_de_samples,
                       max_de_chars_per_sample,
                       num_de_chars))

for i, (en_sample, de_sample) in enumerate(zip(en_samples, de_samples)):
    for char, en_char in enumerate(en_sample):
        encoder_input_data[i, char, en_char_to_int[en_char]] = 1
    for char, de_char in enumerate(de_sample):
        decoder_input_data[i, char, de_char_to_int[de_char]] = 1
        if char > 0 :
            target_data[i, char-1, de_char_to_int[de_char]]  = 1
            
print(f'Shape of encoder_input_data : {encoder_input_data.shape}')
print(f'Shape of decoder_input_data : {decoder_input_data.shape}')
print(f'Shape of target_data        : {target_data.shape}')