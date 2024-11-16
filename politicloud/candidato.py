import matplotlib.pyplot as plt
from wordcloud import WordCloud


# armazena as stopwords em uma lista
stopwords = open('./resources/stopwords.txt', encoding='UTF8').read()
lista_stopwords = stopwords.split()

# define a classe candidato e suas características, além de abrir o arquivo onde os tweets ficam armazenados
class Candidato():
    def __init__(self, nome:str, twitter:str, idade:int, partido:str, escolaridade:str, profissao:str, bio:str, tweets) -> None:
        self.nome = nome
        self.twitter = twitter
        self.idade = idade
        self.partido = partido
        self.escolaridade = escolaridade
        self.profissao = profissao
        self.bio = bio
        self.tweets = open(tweets, encoding='UTF8').read()

# apresenta um resumo do candidato
    def status(self):
        print(
            f"--Candidato(a) a Prefeitura do Município do Rio de Janeiro--\n"
            f"{self.nome}, {self.idade} anos\n"
            f"Partido {self.partido}\n"
            f"{self.profissao}, {self.escolaridade}\n"
            f"{self.bio}\n"
        )

# adiciona o nome do candidato e seu nome de usuário do twitter (com e sem @) na lista de stopwords
    def add_stopwords(self):
        lista2 = [self.nome, self.twitter, self.twitter.lstrip('@')] + self.nome.split()
        nova_lista = lista_stopwords + lista2
        return nova_lista

# cria a wordcloud do objeto, que abrirá como uma imagem estática de fundo preto e letras coloridas
    def create_wordcloud(self):
        wordcloud = WordCloud(
            stopwords=self.add_stopwords(),
            width=700,
            height=700,
        )
        wordcloud.generate(self.tweets)
        plt.figure(figsize=(10,10))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()