'''
Os exemplos de candidatos abaixo, bem como seus tweets, são inteiramente fictícios e foram criados com ajuda de um chatbot com inteligência artificial.
Nenhum dos exemplos tem a pretensão de representar uma pessoa real, apenas arquétipos comuns no cenário político brasileiro.
Nenhum posicionamento, discurso, opinião ou escolha de palavras nas apresentaçãos dos candidatos ou seus tweets é reflexo das opiniões pessoais do aluno. Todos esses materiais foram gerados para fins de execução da aplicação como demonstração do seu funcionamento, em âmbito educacional.
'''
from candidato import Candidato


# Criando instâncias da classe Candidato com as informações geradas
jorge_ribeiro = Candidato(
    53,
    'PRT (Partido Republicano Trabalhista)',
    'Ensino Médio Completo',
    'Policial Militar reformado',
    './resources/cel_jorge_ribeiro.json'
)

ana_mendes = Candidato(
    41,
    'PSP (Partido Socialista do Povo)',
    'Doutora em Ciências Sociais',
    'Professora universitária',
    './resources/ana_mendes_rj.json'
)

fernando_costa = Candidato(
    44,
    'PDL (Partido Democracia e Liberdade)',
    'Graduado em Administração',
    'Empresário do setor de eventos',
    './resources/fernando_costa.json'
)

luciana_souza = Candidato(
    28,
    'PMC (Partido do Movimento Comunista)',
    'Graduada em Serviço Social',
    'Assistente social',
    './resources/luci_sou.json'
)

# iniciando a função da nuvem de palavras

jorge_ribeiro.create_wordcloud()
ana_mendes.create_wordcloud()
fernando_costa.create_wordcloud()
luciana_souza.create_wordcloud()
