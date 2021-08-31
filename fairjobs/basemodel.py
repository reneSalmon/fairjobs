import data
import pickle

class BaseModel(object):

    def __init__(self, df):
        self.df = df

    def fem_words(self, text):
        fh = open("../vocab_fem.pkl", 'rb')
        final_fem_vocab = pickle.load(fh)
        fh.close()

        n_fem_words = 0
        for word in text:
            if word in final_fem_vocab:
                n_fem_words += 1
        return n_fem_words

    def masc_words(self, text):
        fh = open("../vocab_masc.pkl", 'rb')
        final_masc_vocab = pickle.load(fh)
        fh.close()

        n_masc_words = 0
        for word in text:
            if word in final_masc_vocab:
                n_masc_words += 1
        return n_masc_words

    def label_gender(self, row):
        if row['fem_coded'] > 52 :
            return 'feminine'
        elif row['fem_coded'] < 48:
            return 'masculine'
        else:
            return 'neutral'

    def masc_fem_words(self):
        self.df['masc_words'] = self.df['clean_description'].apply(self.masc_words)
        self.df['fem_words'] = self.df['clean_description'].apply(self.fem_words)

        self.df['masc_coded'] = self.df['masc_words']/(self.df['masc_words'] +
                                                       self.df['fem_words'] + 0.001)
        self.df['fem_coded'] = self.df['fem_words']/(self.df['masc_words']
                                                     + self.df['fem_words'] + 0.001)

        self.df.masc_coded = self.df.masc_coded.round(2)*100
        self.df.fem_coded = self.df.fem_coded.round(2)*100
        self.df['gender'] = self.df.apply(lambda row: self.label_gender(row), axis=1)
        return self.df

    def df_to_csv(self):
        self.df.to_csv('../raw_data/data_2021-31-08-cleaned_newds_gd.csv', encoding='utf-8')

if __name__ == '__main__':
    df = data.get_data()
    df_clean = data.clean_df(df)
    print(df_clean.columns)
    model = BaseModel(df_clean)
    model.masc_fem_words()
    model.df_to_csv()
    print(model.df)
