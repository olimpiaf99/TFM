import pandas as pd
import numpy as np

'''
tuit = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\tweet_emotions.csv')
print(tuit)

tuit.groupby(['sentiment']).count()

tuit = tuit.drop(tuit[tuit.sentiment == 'neutral'].index)
tuit = tuit.drop(tuit[tuit.sentiment == 'love'].index)
tuit = tuit.drop(tuit[tuit.sentiment == 'boredom'].index)
tuit = tuit.drop(tuit[tuit.sentiment == 'empty'].index)
tuit = tuit.drop(tuit[tuit.sentiment == 'relief'].index)
tuit = tuit.drop(tuit[tuit.sentiment == 'fun'].index)
tuit = tuit.drop(tuit[tuit.sentiment == 'enthusiasm'].index)

tuit['sentiment'] = tuit['sentiment'].replace(['hate'], 'anger')
tuit['sentiment'] = tuit['sentiment'].replace(['happiness'], 'happy')
tuit['sentiment'] = tuit['sentiment'].replace(['worry'], 'fear')

tuit.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\tweet_emotions.csv')


train = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\train.csv', sep=';')
print(train)

sentiments2 = train.groupby(['sentiment']).count()
print(sentiments2)

val = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\val.csv', sep=';')
print(val)

sentiments3 = val.groupby(['sentiment']).count()
print(sentiments3)

test = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\test.csv', sep=';')
print(test)

sentiments4 = test.groupby(['sentiment']).count()
print(sentiments4)

sets = [train, val, test]
dataset = pd.concat(sets)
dataset.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\full_sentences.csv')

full_sentences = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\full_sentences.csv')
print(full_sentences)
full_sentences = full_sentences.drop(columns = ['numbers'])
'''

'''
emot_final = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\Emotion_final.csv')
print(emot_final)

sentiments5 = emot_final.groupby(['Emotion']).count()
print(sentiments5)

diff_full = set(full_sentences['sentence'])-set(emot_final['Text']) #quitamos a full_sentence las de emot_final y nos da 0, es decir, todas las 20000 de full_sentences estan en emot_final
diff_emot = set(emot_final['Text'])-set(full_sentences['sentence']) #quitamos a emot_final las de full_sentences y nos da 1457, que es la diferencia
print(diff_full, diff_emot)
#Nos quedamos con el dataset emot_final porque incluye todas las frases de full_sentences.
'''

'''
#reading no cause file and extracting only the anger and surprise emotions
no_cause = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\No Cause.csv', sep = ';')
print(no_cause.groupby('Emotion').count())

anger = no_cause[no_cause['Emotion']== 'anger']
surprise = no_cause[no_cause['Emotion']== 'surprise']

anger.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\anger_texts.csv')
surprise.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\surprise_texts.csv')
'''

'''
#creating text_emotion dataset
dialogue_emotions = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\dialogues_emotion.csv', sep = ';')
dialogue_emotions.info()
dialogue_text = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\dialogues_text.csv', sep = ';')
dialogue_text.info()

text_emotion = pd.merge(dialogue_emotions, dialogue_text, on='id')
print(text_emotion)
text_emotion.info()
text_emotion.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\text_emotions.csv')
'''

'''
#guardar solo las rows con emociones 1 y 6

text_emotion = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\text_emotions.csv')
text_emotion.info()

anger_emotions = text_emotion[text_emotion.Emotion.str.contains("1", regex = False)]
anger_emotions.info()

surprise_emotions = text_emotion[text_emotion.Emotion.str.contains("5", regex = False)]
surprise_emotions.info()

anger_surprise_emotions = pd.concat([anger_emotions, surprise_emotions])
anger_surprise_emotions.info()
anger_surprise_emotions = anger_surprise_emotions.drop_duplicates()
anger_surprise_emotions.info()


anger_surprise_emotions = anger_surprise_emotions.drop('Unnamed: 0', axis = 1)
anger_surprise_emotions = anger_surprise_emotions.drop('Unnamed: 0.1', axis = 1)
print(anger_surprise_emotions)

#separo la columna de emociones y elimino el espacio del final de cada row
split_e = anger_surprise_emotions.drop('Text', axis = 1)
split_e['Emotion'] = split_e['Emotion'].str[:-1]
print(split_e)

#separo cada numero en una fila de la tabla y reestablezco los ids
split_enew = split_e.set_index(['id']).apply(lambda x: x.str.split(' ').explode()).reset_index()
split_enew['id'] = range(1, len(split_enew) + 1)
print(split_enew)

#separo la columna de text y elimino el ultimo __eou__
split_t = anger_surprise_emotions.drop('Emotion', axis = 1)
split_t['Text'] = split_t['Text'].str[:-7]
print(split_t)

#separo cada tramo de la conver y reestablezco los ids
split_tnew = split_t.set_index(['id']).apply(lambda x: x.str.split('__eou__').explode()).reset_index()
split_tnew['id'] = range(1, len(split_tnew) + 1)
print(split_tnew)

#junto los dos df separados de nuevo
anger_surprise_emotions = pd.merge(split_enew, split_tnew, on = 'id')
print(anger_surprise_emotions)

anger_surprise_emotions.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\anger_surprise_emotions.csv')

#ELIMINAR SENTIMIENTOS QUE NO SEAN 1 Y 5
anger_surprise_emotions = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\anger_surprise_emotions.csv')

print(anger_surprise_emotions.groupby('Emotion').count())

no_0 = anger_surprise_emotions.drop(anger_surprise_emotions[anger_surprise_emotions.Emotion == 0].index)
no_02 = no_0.drop(no_0[no_0.Emotion == 2].index)
no_023 = no_02.drop(no_02[no_02.Emotion == 3].index)
no_0234 = no_023.drop(no_023[no_023.Emotion == 4].index)
no_02345 = no_0234.drop(no_0234[no_0234.Emotion == 5].index)

ang_sur = no_02345.drop('Unnamed: 0', axis = 1)
print(ang_sur.groupby('Emotion').count())

ang_sur.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\ang_sur_emot.csv')
'''

'''
#Load friends dialogues datasets
train_friends = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\train_friends.csv')
dev_friends = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\dev_friends.csv')
test_friends = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\test_friends.csv')

#Drop unnecessary columns
train_friends = train_friends.drop(['Speaker', 'Sentiment', 'Dialogue_ID', 'Utterance_ID', 'Season', 'Episode', 'StartTime', 'EndTime'], axis = 1)
dev_friends = dev_friends.drop(['Speaker', 'Sentiment', 'Dialogue_ID', 'Utterance_ID', 'Season', 'Episode', 'StartTime', 'EndTime'], axis = 1)
test_friends = test_friends.drop(['Speaker', 'Sentiment', 'Dialogue_ID', 'Utterance_ID', 'Season', 'Episode', 'StartTime', 'EndTime'], axis = 1)

train_friends.groupby('Emotion').count()
dev_friends.groupby('Emotion').count()
test_friends.groupby('Emotion').count()

#Drop all emotions except anger and surprise
train_friends_drop = train_friends.drop(train_friends[train_friends.Emotion == 'neutral'].index)
train_friends_drop = train_friends_drop.drop(train_friends_drop[train_friends_drop.Emotion == 'fear'].index)
train_friends_drop = train_friends_drop.drop(train_friends_drop[train_friends_drop.Emotion == 'sadness'].index)
train_friends_drop = train_friends_drop.drop(train_friends_drop[train_friends_drop.Emotion == 'joy'].index)
train_friends_drop = train_friends_drop.drop(train_friends_drop[train_friends_drop.Emotion == 'disgust'].index)

dev_friends_drop = dev_friends.drop(dev_friends[dev_friends.Emotion == 'neutral'].index)
dev_friends_drop = dev_friends_drop.drop(dev_friends_drop[dev_friends_drop.Emotion == 'fear'].index)
dev_friends_drop = dev_friends_drop.drop(dev_friends_drop[dev_friends_drop.Emotion == 'sadness'].index)
dev_friends_drop = dev_friends_drop.drop(dev_friends_drop[dev_friends_drop.Emotion == 'joy'].index)
dev_friends_drop = dev_friends_drop.drop(dev_friends_drop[dev_friends_drop.Emotion == 'disgust'].index)

test_friends_drop = test_friends.drop(test_friends[test_friends.Emotion == 'neutral'].index)
test_friends_drop = test_friends_drop.drop(test_friends_drop[test_friends_drop.Emotion == 'fear'].index)
test_friends_drop = test_friends_drop.drop(test_friends_drop[test_friends_drop.Emotion == 'sadness'].index)
test_friends_drop = test_friends_drop.drop(test_friends_drop[test_friends_drop.Emotion == 'joy'].index)
test_friends_drop = test_friends_drop.drop(test_friends_drop[test_friends_drop.Emotion == 'disgust'].index)

# concat all
sets = [train_friends_drop, dev_friends_drop, test_friends_drop]
ang_sur_friends = pd.concat(sets)
ang_sur_friends.groupby('Emotion').count()
ang_sur_friends.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\ang_sur_friends.csv')
'''

'''
data_google = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\full_dataset_google\goemotions_1.csv')

data_google.info()
data_google.groupby('surprise').count()

data_google = data_google[['text', 'anger', 'surprise']]

data_google_ang = data_google.drop('surprise', axis = 1)
data_google_sur = data_google.drop('anger', axis = 1)

data_google_ang = data_google_ang.drop(data_google_ang[data_google_ang.anger == 0].index)
data_google_sur = data_google_sur.drop(data_google_sur[data_google_sur.surprise == 0].index)

data_google_ang['anger'] = 'anger'
data_google_ang = data_google_ang.rename(columns={'anger': 'Emotion'})
data_google_sur['surprise'] = 'surprise'
data_google_sur = data_google_sur.rename(columns={'surprise': 'Emotion'})

sets = [data_google_ang, data_google_sur]
google_ang_sur = pd.concat(sets)
google_ang_sur.groupby('Emotion').count()

google_ang_sur.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\google_ang_sur.csv')

###################################################

data_google = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\full_dataset_google\goemotions_2.csv')

data_google.info()
data_google.groupby('surprise').count()

data_google = data_google[['text', 'surprise']]

data_google_sur = data_google.drop(data_google[data_google.surprise == 0].index)

data_google_sur['surprise'] = 'surprise'
data_google_sur = data_google_sur.rename(columns={'surprise': 'Emotion'})

data_google_sur.groupby('Emotion').count()

data_google_sur.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\data_google_sur.csv')

############################################################################################

data_google = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\full_dataset_google\goemotions_3.csv')

data_google.info()
data_google.groupby('surprise').count()

data_google = data_google[['text', 'surprise']]

data_google_sur = data_google.drop(data_google[data_google.surprise == 0].index)

data_google_sur['surprise'] = 'surprise'
data_google_sur = data_google_sur.rename(columns={'surprise': 'Emotion'})

data_google_sur.groupby('Emotion').count()

data_google_sur.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\data_google_sur2.csv')
'''

# Mergeamos todos los datasets que vamos a usar

emot_final = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\Emotion_final.csv')
tweet = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\tweet_emotions.csv')
ang_sur_emot = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\ang_sur_emot.csv')
ang_sur_friends = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\ang_sur_friends.csv')
ang_texts = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\anger_texts.csv')
ang_tweets = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\anger_tweets.csv', sep = ';')
sur_google = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\data_google_sur.csv')
sur_google2 = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\data_google_sur2.csv')
ang_sur_google = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\google_ang_sur.csv')
sur_texts = pd.read_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\surprise_texts.csv')

#fix emot_final
emot_final = emot_final.drop(emot_final[emot_final.Emotion == 'love'].index)
emot_final.info()
emot_final.groupby(['Emotion']).count()

#fix tweet
tweet = tweet.drop(['Unnamed: 0', 'tweet_id'], axis = 1)
tweet = tweet.rename(columns={'sentiment': 'Emotion'})
tweet = tweet.rename(columns={'content': 'Text'})
tweet.info()
tweet.groupby(['Emotion']).count()

#fix ang_sur_emot
ang_sur_emot = ang_sur_emot.drop(['Unnamed: 0', 'id'], axis = 1)
ang_sur_emot['Emotion'] = ang_sur_emot['Emotion'].replace([1], 'anger')
ang_sur_emot['Emotion'] = ang_sur_emot['Emotion'].replace([6], 'surprise')
ang_sur_emot.info()
ang_sur_emot.groupby(['Emotion']).count()

#fix ang_sur_friends
ang_sur_friends = ang_sur_friends.drop(['Unnamed: 0', 'Sr No.'], axis = 1)
ang_sur_friends = ang_sur_friends.rename(columns={'Utterance': 'Text'})
ang_sur_friends.info()
ang_sur_friends.groupby(['Emotion']).count()

#fix ang_texts
ang_texts = ang_texts.drop(['Unnamed: 0'], axis=1)
ang_texts.info()
ang_texts.groupby(['Emotion']).count()

#fix ang_tweets
ang_tweets = ang_tweets.drop(['tweet_id'], axis=1)
ang_tweets = ang_tweets.rename(columns={'content': 'Text'})
ang_tweets = ang_tweets.rename(columns={'sentiment': 'Emotion'})
ang_tweets['Emotion'] = 'anger'
ang_tweets.info()
ang_tweets.groupby(['Emotion']).count()

#fix sur_google
sur_google = sur_google.drop(['Unnamed: 0'], axis=1)
sur_google = sur_google.rename(columns={'text': 'Text'})
sur_google.info()
sur_google.groupby(['Emotion']).count()

#fix sur_google2
sur_google2 = sur_google2.drop(['Unnamed: 0'], axis=1)
sur_google2 = sur_google2.rename(columns={'text': 'Text'})
sur_google2.info()
sur_google2.groupby(['Emotion']).count()

#fix ang_sur_google
ang_sur_google = ang_sur_google.drop(['Unnamed: 0'], axis=1)
ang_sur_google = ang_sur_google.rename(columns={'text': 'Text'})
ang_sur_google.info()
ang_sur_google.groupby(['Emotion']).count()

#fix sur_texts
sur_texts = sur_texts.drop(['Unnamed: 0'], axis=1)
sur_texts.info()
sur_texts.groupby(['Emotion']).count()

#concat them all
final_dataset = pd.concat([ang_sur_emot, ang_sur_friends, ang_sur_google, ang_texts, ang_tweets, emot_final,
                          sur_google, sur_google2, sur_texts, tweet], axis=0)

final_dataset = final_dataset.append({"Emotion":"surprise", "Text":"My sister just told me we're gonna have a baby!"}, ignore_index=True)
final_dataset.info()
final_dataset.groupby(['Emotion']).count()
final_dataset.to_csv(r'C:\Users\olimp\OneDrive\Documentos\TFM EDEM\datasets_multiclass_sent_analysis\used\final_dataset.csv')

