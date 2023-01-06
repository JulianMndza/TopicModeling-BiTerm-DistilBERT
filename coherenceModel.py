
if __name__ == '__main__':
    import re
    from gensim.corpora import Dictionary
    from gensim.models import CoherenceModel
    texts = open('preprocessed_comments', encoding="utf8").read().splitlines()
    tokenizer = lambda s: re.findall('\w+', s.lower())
    text = [tokenizer(t) for t in texts]
    # Input topics from BiTerm/BerTopic
    #[0]topic number [1]top words
    top = [['lockdown', 'lang', 'pasaway', 'jan'],
           ['yung', 'kasi', 'mayor', 'meron'],
           ['city', 'like', 'bike', 'good', 'infected']]
    # Creating a dictionary with the vocabulary
    word2id = Dictionary(text)
    # Coherence model
    # UMass Coherence: Coherence(measure='u_mass')
    # C_V Coherence: Coherence(measure='c_v')
    # UCI Coherence: Coherence(measure='c_uci')
    # NPMI Coherence: Coherence(measure='c_npmi')
    cm = CoherenceModel(topics=top,
                        texts=text,
                        coherence='c_uci',
                        dictionary=word2id)

    coherence_per_topic = cm.get_coherence_per_topic()
    print('Topic Coherence:' + str(coherence_per_topic))
    coherence = cm.get_coherence()
    print('Average coherence:' + str(coherence))