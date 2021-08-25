from gensim.models import Word2Vec
import data
from vocabulary import masc_vocab, fem_vocab

class BaseModel(object):

    def __init__(self, df):
        self.df = df

    def word2vec(self):

        self.word2vec_description = Word2Vec(sentences=self.df['clean_description'],
                                             vector_size=50,
                                             min_count=1)
        return self

    def masc_similar_words(self, text):
        # simil_masc_vocab = []
        # match_masc_vocab = []

        n_simil_masc = 0
        n_match_masc = 0

        for word in text:
            for masc_word in masc_vocab:
                if masc_word in self.word2vec_description.wv.key_to_index:
                    if self.word2vec_description.wv.similarity(word, masc_word) > 0.9 and\
                    self.word2vec_description.wv.similarity(word, masc_word) < 0.99:
                        n_simil_masc += 1
                        # simil_masc_vocab.append((word, masc_word))
                        # simil_masc_vocab = list(dict.fromkeys(simil_masc_vocab))
                if word.find(masc_word) == 0:
                    n_match_masc += 1
                    # match_masc_vocab.append((word, masc_word))
                    # match_masc_vocab = list(dict.fromkeys(match_masc_vocab))

        return (n_simil_masc + n_match_masc)

    def fem_similar_words(self, text):
        # simil_fem_vocab = []
        # match_fem_vocab = []

        n_simil_fem = 0
        n_match_fem = 0

        for word in text:
            for fem_word in fem_vocab:
                if fem_word in self.word2vec_description.wv.key_to_index:
                    if self.word2vec_description.wv.similarity(word, fem_word) > 0.9 and\
                    self.word2vec_description.wv.similarity(word, fem_word) < 0.99:
                        n_simil_fem += 1
                        # simil_fem_vocab.append((word, fem_word))
                        # simil_fem_vocab = list(dict.fromkeys(simil_fem_vocab))
                if word.find(fem_word) == 0:
                    n_match_fem += 1
                    # match_fem_vocab.append((word, fem_word))
                    # match_fem_vocab = list(dict.fromkeys(match_fem_vocab))

        return (n_simil_fem + n_match_fem)


    def masc_fem_words(self):
        self.df['masc_words'] = self.df['clean_description'].apply(self.masc_similar_words)
        self.df['fem_words'] = self.df['clean_description'].apply(self.fem_similar_words)
        self.df['masc_coded'] = self.df['masc_words']/(self.df['masc_words'] + self.df['fem_words'])
        self.df['fem_coded'] = self.df['fem_words']/(self.df['masc_words'] + self.df['fem_words'])
        self.df = self.df.round(2)*100
        return self.df

if __name__ == '__main__':
    df = data.get_data()
    df_clean = data.clean_df(df)
    print(df_clean.columns)
    model = BaseModel(df_clean)
    model.word2vec()
    model.masc_fem_words()
    print(model.df)
