from sentence_transformers import SentenceTransformer
from umap import UMAP
from hdbscan import HDBSCAN
from bertopic import BERTopic
import numpy as np
from tqdm import tqdm
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models.coherencemodel import CoherenceModel
from gensim.corpora.dictionary import Dictionary


#resets the visualization html
if os.path.exists("TopicModels.html"):
   os.remove("TopicModels.html")

#Load data set
prefix = 'Getting comments'
pbar = tqdm(total=100, position=0, leave=True) #progress bar in terminal
pbar.set_description(prefix)
pbar.update(2)
data = open('preprocessed_comments.csv', encoding="utf8").read().splitlines()

#region Embeddings and Sentence Transformers
#if a new data set is loaded then need to change the embeddings.npy uncomment and run once after running once comment this section again
# embedding_model = SentenceTransformer("sentence-transformers/distiluse-base-multilingual-cased-v2")
# embeddings = embedding_model.encode(data)
# np.save('embeddings.npy', embeddings)
#endregion

#Set up UMAP and HDBSCAN models for dimension reductions and clustering
prefix = 'Progress: Setting UMAP models and HDBSCAN models'
pbar.set_description(prefix)
pbar.update(18)
umap_model = UMAP(n_neighbors=3, n_components=3, min_dist=0.05)
hdbscan_model = HDBSCAN(min_cluster_size=5, min_samples=5, gen_min_span_tree=True, prediction_data=True)


#loads embeddings from embedding model
prefix = 'Loading embeddings'
pbar.set_description(prefix)
pbar.update(20)
all_embeddings = np.load('embeddings.npy')

#creates BERT model for topic modeling and fits the model to the data set
prefix = 'Creating BERT Topic Model'
pbar.set_description(prefix)
pbar.update(30)

topic_model = BERTopic(
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    top_n_words=5,
    language='multilingual',
    calculate_probabilities=True,
    verbose=True
)


prefix = 'Fitting the model'
pbar.set_description(prefix)
pbar.update(10)
topics, probs = topic_model.fit_transform(data, embeddings=all_embeddings)

#Getting Topics for visualization and processing
prefix = 'Getting Topics'
pbar.set_description(prefix)
pbar.update(10)

freq = topic_model.get_topic_info()


top_topics = freq.head(10) #topic_model.get_topic(10)
len_of_topics = len(top_topics)

prefix = 'Visualizing'
pbar.set_description(prefix)
pbar.update(5)

fig1 = topic_model.visualize_topics(top_n_topics=len_of_topics)
fig2 = topic_model.visualize_barchart(top_n_topics=len_of_topics)
fig3 = topic_model.visualize_distribution(probs[200], min_probability=0.001)
fig4 = topic_model.visualize_hierarchy(top_n_topics=len_of_topics)
fig5 = topic_model.visualize_heatmap(top_n_topics=len_of_topics, width=1000, height=1000)
fig6 = topic_model.visualize_term_rank()

with open('TopicModels.html', 'a') as f:
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig5.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig6.to_html(full_html=False, include_plotlyjs='cdn'))

print("\033[A                                                                                                                                                                     \033", end="\r")
print(" ", end="\r")
prefix = 'Topic Modeling Complete'
pbar.set_description(prefix)
pbar.update(5)
pbar.close()


#Coherence Metric
print("\n\n==========================================COHERENCE=============================================\n\n")

#Reg exp for tokenizing the data set
tokenizer = lambda s: re.findall('\w+', s.lower())
text = [tokenizer(t) for t in data]

# Getting Topics
all_topics = topic_model.get_topics()
top = []
keys = []
for x in range(10):
    keys.append(freq['Topic'].head(10)[x])

#Tokenizing
prefix = 'Getting Topics'
pbar2 = tqdm(total=len(keys), position=0, leave=True)
pbar2.set_description(prefix)
for key in tqdm(keys, desc='Getting Topics', position=0, leave=True):
    values = all_topics[key]
    topic_1 = []
    for value in tqdm(values, desc='Retrieving Values in topic ' + str(key), position=0, leave=True):
        topic_1.append(value[0])
    top.append(topic_1)

# Creating a dictionary with the vocabulary
word2id = Dictionary(text)
vec = CountVectorizer()
X = vec.fit_transform(data).toarray()
vocab = np.array(vec.get_feature_names())
# Coherence model
cm = CoherenceModel(topics=top, texts=text, coherence='u_mass', dictionary=word2id)
coherence_per_topic = cm.get_coherence_per_topic()

#Results
print("\n==========================================COHERENCE RESULTS=============================================\n")
for index, x in enumerate(coherence_per_topic):
    print("topic %2d : %5.2f" % (index + 1, x))

coherence = cm.get_coherence()
print(coherence)
