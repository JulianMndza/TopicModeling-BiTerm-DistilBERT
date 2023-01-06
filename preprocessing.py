### Data Preprocessing ###

# Import needed libraries
import pandas as pd
import re
import string
import warnings
import nltk
from nltk.corpus import stopwords
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load in Facebook LGU Comments dataset
comments = pd.read_csv('preprocessed_comments.csv')
comments = comments[['Comment']]
print("STATUS: Data before preprocessing")
print(comments)

def preprocess(text):
    # Conversion to lowercase
    preprocessed_text = text.lower()
    # Removal of Links
    preprocessed_text = re.sub('https:\/\/\S+', '', preprocessed_text)
    # Removal of Symbols
    preprocessed_text = re.sub(r'[^\w]', ' ', preprocessed_text)
    # Removal of Numbers
    preprocessed_text = re.sub('\w*\d\w*', '', preprocessed_text)
    # Removal of Extra Spaces
    preprocessed_text = re.sub(' +', ' ', preprocessed_text)
    return preprocessed_text
comments['Comment'] = comments.Comment.apply(lambda x: preprocess(x))

spelling_dictionary = {'sched':'schedule',
'pong':'po ng',
'lng':'lang',
'maynila':'manila',
'ung':'yung',
'nyo':'niyo',
'nman':'naman',
'brgy':'barangay',
'brngy':'barangay',
'nya':'niya',
'yorme':'mayor',
'nyu':'niyo',
'tyo':'tayo',
'hnd':'hindi',
'n':'na',
'kht':'kahit',
'kc':'kasi',
'tlga':'talaga',
'khit':'kahit',
'nio':'niyo',
'nmin':'namin',
'govt':'government',
'bkt':'bakit',
'bkit':'bakit',
'gud':'good',
'thx':'thanks',
'rip':'rest in peace',
'bka':'baka',
'kmi':'kami',
'wla':'wala',
'dpat':'dapat',
'pwd':'pwede',
'kc':'kasi',
'dpt':'dapat'
}

# Spelling Correction                       
def spelling_correction(text):
    for k, v in spelling_dictionary.items():
        text = re.sub(rf'\b{k}\b', v, text)
    return text
for c in range(len(comments['Comment'])):
    comments['Comment'][c] = spelling_correction(comments['Comment'][c])


stop_words_en = set(stopwords.words('english'))
pattern_en = r'\b(?:{})\b'.format('|'.join(stop_words_en))
stop_words_fil = ['akin',
 'aking',
 'ako',
 'alin',
 'amin',
 'aming',
 'ang',
 'ano',
 'anumang',
 'apat',
 'at',
 'atin',
 'ating',
 'ay',
 'ba',
 'bababa',
 'bago',
 'bakit',
 'bawat',
 'bilang',
 'dahil',
 'dalawa',
 'dapat',
 'din',
 'dito',
 'doon',
 'gagawin',
 'ginagawa',
 'ginawa',
 'ginawang',
 'gumawa',
 'gusto',
 'habang',
 'hanggang',
 'hindi',
 'huwag',
 'iba',
 'ibaba',
 'ibabaw',
 'ibig',
 'ikaw',
 'ilagay',
 'ilalim',
 'ilan',
 'inyong',
 'isa',
 'isang',
 'itaas',
 'ito',
 'iyo',
 'iyon',
 'iyong',
 'ka',
 'kahit',
 'kailanman',
 'kami',
 'kanila',
 'kanilang',
 'kanino',
 'kanya',
 'kanyang',
 'kapag',
 'kapwa',
 'karamihan',
 'katiyakan',
 'katulad',
 'kaya',
 'kaysa',
 'ko',
 'kong',
 'kulang',
 'kumuha',
 'kung',
 'laban',
 'lahat',
 'lamang',
 'likod',
 'lima',
 'maaari',
 'maaaring',
 'maging',
 'mahusay',
 'makita',
 'marami',
 'marapat',
 'masyado',
 'may',
 'mayroon',
 'mga',
 'minsan',
 'mismo',
 'mula',
 'muli',
 'na',
 'nabanggit',
 'naging',
 'nagkaroon',
 'nais',
 'nakita',
 'naman',
 'namin',
 'napaka',
 'narito',
 'nasa',
 'nasaan',
 'ng',
 'ngayon',
 'ni',
 'nila',
 'nilang',
 'nito',
 'niya',
 'niyang',
 'noon',
 'o',
 'pa',
 'paano',
 'pababa',
 'paggawa',
 'pagitan',
 'pagkakaroon',
 'pagkatapos',
 'palabas',
 'pamamagitan',
 'panahon',
 'pangalawa',
 'para',
 'paraan',
 'pareho',
 'pataas',
 'pero',
 'pumunta',
 'pumupunta',
 'po',
 'rin',
 'sa',
 'saan',
 'sabi',
 'sabihin',
 'sarili',
 'si',
 'sila',
 'sino',
 'siya',
 'tatlo',
 'tayo',
 'tulad',
 'tungkol',
 'una',
 'walang']
pattern_fil = r'\b(?:{})\b'.format('|'.join(stop_words_fil))

# Removal of Stop Words
comments['Comment'] = comments['Comment'].str.replace(pattern_en, '')
comments['Comment'] = comments['Comment'].str.replace(r'\s+', ' ')
comments['Comment'] = comments['Comment'].str.replace(pattern_fil, '')
comments['Comment'] = comments['Comment'].str.replace(r'\s+', ' ')

# Removal of Duplicates
comments = comments[comments['Comment'] != ' ']
comments = comments[comments['Comment'] != ''].drop_duplicates(subset = ['Comment'])

# Removal of Comments with less than 3 words
for c in comments['Comment']:
    if len(c.split()) < 3:
        comments = comments[comments['Comment'] != c]

# Save preprocessed dataset
print("STATUS: Data after preprocessing...")
print(comments)
comments.to_csv('preprocessed_comments.csv', index=False)
print('STATUS: Data saved...')