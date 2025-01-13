import matplotlib.pyplot as plt
import json
from wordcloud import WordCloud


# inicia a classe Candidato, recebendo alguns valores manuais e carregando o json para receber os valores da fonte (Twitter)
class Candidato():
    def __init__(self, idade:int, partido:str, escolaridade:str, profissao:str, source:str) -> None:
        self.idade = idade
        self.partido = partido
        self.escolaridade = escolaridade
        self.profissao = profissao
        self.source = source
        with open(source, 'r', encoding='UTF8') as file:
            data = json.load(file)
        self.nome = data['user']['name']
        self.twitter = '@' + data['user']['screen_name']
        self.bio = data['user']['description']
        self.tweets = {}


# carrega os tweets do arquivo para dentro do objeto Candidato na forma de um dicionário, usando os campos "id" e "full_text" do arquivo json
    def load_tweets(self):
        with open(self.source, 'r', encoding='UTF8') as file:
            data = json.load(file)
            
        for tweet in data['tweets']:
            self.tweets.update({tweet['id']: tweet['full_text']})


# apresenta um resumo do candidato
    def status(self):
        print(
            f"--Candidato(a) a Prefeitura do Município do Rio de Janeiro--\n"
            f"{self.nome}, {self.idade} anos\n"
            f"Partido {self.partido}\n"
            f"{self.profissao}, {self.escolaridade}\n"
            f"{self.bio}\n"
        )


# cria a lista de stopwords (termos a serem ignorados) e adiciona a ela o nome do próprio candidato e o seu próprio nome de usuário (com e sem @)
    def add_stopwords(self):
        stopwords = open('./resources/stopwords.txt', encoding='UTF8').read()
        lista_stopwords = stopwords.split()
        lista2 = [self.nome, self.twitter, self.twitter.lstrip('@')] + self.nome.split()
        nova_lista = lista_stopwords + lista2
        return nova_lista


# cria a wordcloud do objeto, que abrirá como uma imagem estática de fundo preto e letras coloridas
    def create_wordcloud(self):
        self.load_tweets()
        raw_txt = ''
        for tweet_txt in self.tweets.values():
            raw_txt += tweet_txt
        
        wordcloud = WordCloud(
            stopwords=self.add_stopwords(),
            width=700,
            height=700,
        )
        wordcloud.generate(raw_txt)
        plt.figure(figsize=(10,10))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
