





import pickle, pandas as pd


# IEMOCAP_features_raw = \
#     pickle.load(open('./iemocap/IEMOCAP_features_raw.pkl', 'rb'), \
#                 encoding='latin1')

# print(IEMOCAP_features_raw)
# print(len(IEMOCAP_features_raw)) # 9

# for i in IEMOCAP_features_raw:
#     print(i)


# print(IEMOCAP_features_raw[0]) # conv_id: [utterance_id, utterance_id]
# for k,v in IEMOCAP_features_raw[0].items():
#     print(k,v)
'''
{
Ses03M_impro08b ['Ses03M_impro08b_M000', 'Ses03M_impro08b_F001', 'Ses03M_impro08b_M001', ...],
Ses05M_impro02 ['Ses05M_impro02_M000', 'Ses05M_impro02_M001', 'Ses05M_impro02_M007', ...],
...
}
'''

# print(len(IEMOCAP_features_raw[0])) # 151
# print(len(IEMOCAP_features_raw[0]["Ses03M_impro08b"])) # 42
# print(len(IEMOCAP_features_raw[0]["Ses05M_impro02"])) # 29


# print(IEMOCAP_features_raw[1]) # conv_id: [sex, sex]
# for k,v in IEMOCAP_features_raw[1].items():
#     print(k,v)
'''
{
Ses03M_impro08b ['M', 'F', 'M', 'F', 'M', 'F', 'M',  ...],
Ses05M_impro02 ['M', 'M', 'M', 'F', 'M', 'M', 'M', 'M', ...],
...
}
'''

# print(IEMOCAP_features_raw[2]) # conv_id: [label, label]
# for k,v in IEMOCAP_features_raw[2].items():
#     print(k,v)
'''
{
Ses03M_impro08b [2, 5, 2, 5, 2, 5, 2, 5, ...],
Ses05M_impro02 [1, 1, 1, 5, 5, 1, ...],
...
}
'''



# print(IEMOCAP_features_raw[3]) # conv_id: [array, array]
# for k,v in IEMOCAP_features_raw[3].items():
#     print(k,v)
'''
{
Ses03M_impro08b [array([ -6.6317444 ,   7.865 ...], array([ -6.6317444 ,   7.865 ...], ...
Ses05M_impro02 [array([ -6.6317444 ,   7.865 ...], array([ -6.6317444 ,   7.865 ...], ...
...
}
'''



# print(IEMOCAP_features_raw[4]) # conv_id: [label, label]
# for k,v in IEMOCAP_features_raw[4].items():
#     print(k,v)
'''
{
Ses03M_impro08b [2, 5, 2, 5, 2, 5, 2, 5, ...],
Ses05M_impro02 [1, 1, 1, 5, 5, 1, ...],
...
}
'''


# print(IEMOCAP_features_raw[5]) # conv_id: [label, label]
# for k,v in IEMOCAP_features_raw[5].items():
#     print(k,v)
'''
{
Ses03M_impro08b [2, 5, 2, 5, 2, 5, 2, 5, ...],
Ses05M_impro02 [1, 1, 1, 5, 5, 1, ...],
...
}
'''

# print(IEMOCAP_features_raw[6]) # conv_id: [utterance, utterance]
# for k,v in IEMOCAP_features_raw[6].items():
#     print(k,v)
'''
{
Ses03M_impro08b ['Hello?', "Oh God I finally got...you know how long I've been waiting on line?  You put on hold for like five hours.  Geez.", "I'm sorry ma'am., ...],
Ses05M_impro02 ["Sweetheart, I've got to tell you something.  I just got a call.  I'm going to Iraq.", "I know  ...],
...
}
'''



# print(IEMOCAP_features_raw[7]) #
'''
{'Ses01F_script02_1', 'Ses04F_impro02', 'Ses02F_impro08', 'Ses02F_impro05', 'Ses04F_script01_2', ...
'''
# print(len(IEMOCAP_features_raw[7])) # 120


# print(IEMOCAP_features_raw[8]) #
'''
{'Ses05F_impro01', 'Ses05M_script01_1b', 'Ses05M_script02_2', 'Ses05F_script02_1', ...
'''
# print(len(IEMOCAP_features_raw[8])) # 31




conversation_length = \
    pickle.load(open('./iemocap/train/conversation_length.pkl', 'rb'), \
                encoding='latin1')
print("conversation_length: ", conversation_length)
print(len(conversation_length)) # 96
'''
[52, 37, 28, 18, 57, 87, 38, 77, 35, 26,
'''

labels = \
    pickle.load(open('./iemocap/train/labels.pkl', 'rb'), \
                encoding='latin1')
print("labels: ", labels)
print(len(labels)) # 96
'''
[[5, 5, 2, 5, 5, 5, 5
'''

sentence_length = \
    pickle.load(open('./iemocap/train/sentence_length.pkl', 'rb'), \
                encoding='latin1')
print("sentence_length: ", sentence_length)
print(len(sentence_length)) # 96
'''
[[18, 30, 10, 12, 10, 17, 26, 19, 3, 5, 10, 30, 8, 
'''


sentences = \
    pickle.load(open('./iemocap/train/sentences.pkl', 'rb'), \
                encoding='latin1')
# print("sentences: ", sentences)
print("sentences[0]: ", sentences[0])

print(len(sentences)) # 96
'''
[[['thank', 'you', 'for', 'calling',  , '
'''
'''
[['thank', 'you', 'for', 'calling',  , '
'''



video_id = \
    pickle.load(open('./iemocap/train/video_id.pkl', 'rb'), \
                encoding='latin1')
print("video_id: ", video_id)
print(len(video_id)) # 96
'''
['Ses04M_impro08', 'Ses02M_impro04', 'Ses01F_impro07', 'Ses03F_script03_1', 
'''


video_id = \
    pickle.load(open('./iemocap/valid/video_id.pkl', 'rb'), \
                encoding='latin1')

print("video_id: ", video_id)
print(len(video_id)) # 24




video_id = \
    pickle.load(open('./iemocap/test/video_id.pkl', 'rb'), \
                encoding='latin1')

print("video_id: ", video_id)
print(len(video_id)) # 31




































