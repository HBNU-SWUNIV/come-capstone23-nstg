
import torch
import torch.nn as nn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from torch.autograd import Variable

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


print(device)

packet_data = pd.read_csv('Deauth_packet_co.csv')

packet_data = packet_data.drop(columns=['No.', 'Time','Protocol', 'Length'])

packet_data.rename(columns={'Unnamed: 7': "Label"}, inplace=True)

packet_data.isna()

packet_data = packet_data.fillna("X")

packet_data.isna()

import re

def remove_special_characters(text):
    cleaned_text = re.sub(r'[^\w\s]', '', str(text)) 
    return cleaned_text


clear_packet = packet_data.applymap(remove_special_characters)

packet_data = clear_packet

clear_packet

def remove_SNFN(text):
    NoSNFN_text = re.sub(r'SN\d+\sFN0', '', str(text))
    return NoSNFN_text

clear_packet = packet_data.applymap(remove_SNFN)

clear_packet

for column in clear_packet.columns:
    if clear_packet[column].dtype == 'object':
        clear_packet[column] = clear_packet[column].astype(bytes)

print(clear_packet.dtypes)
clear_packet

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

target_Info = b'Deauthentication  Flags'



def label_packet(row):
    if row["Info"] == target_Info :
        return 1
    else:
        return 0


clear_packet["Label"] = clear_packet.apply(label_packet, axis=1)


clear_packet

clear_packet.to_csv("labeled_packets_neeeew.csv", index=False)

print("Packets saved to 'labeled_packets.csv'")