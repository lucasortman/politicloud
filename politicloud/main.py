'''
Os exemplos de candidatos abaixo, bem como seus tweets, são inteiramente fictícios e foram criados com ajuda de um chatbot com inteligência artificial.
Nenhum dos exemplos tem a pretensão de representar uma pessoa real, apenas arquétipos comuns no cenário político brasileiro.
Nenhum posicionamento, discurso, opinião ou escolha de palavras nas apresentaçãos dos candidatos ou seus tweets é reflexo das opiniões pessoais do aluno. Todos esses materiais foram gerados para fins de execução da aplicação como demonstração do seu funcionamento, em âmbito educacional.
'''
import numpy as np
import pandas as pd
from candidato import Candidato, lista_stopwords


# Criando instâncias da classe Candidato com as informações geradas


jorge_ribeiro = Candidato(
    'Jorge Luís Ribeiro',
    '@cel_jorge_ribeiro',
    53,
    'PRT (Partido Republicano Trabalhista)',
    'Ensino Médio Completo',
    'Policial Militar reformado',
    'Jorge Luís Ribeiro, policial militar reformado, é uma figura popular nas comunidades da Zona Norte, onde já liderou operações de segurança e combate ao tráfico de drogas. Ele promete aumentar significativamente o número de policiais nas ruas e garantir o retorno da ordem nas áreas dominadas pela criminalidade. Jorge é evangélico praticante e crê que os valores religiosos podem ser fundamentais para a transformação social. Adepto do futebol amador, organiza campeonatos entre jovens da periferia.',
    './resources/jorge-luis-ribeiro.txt'
)

ana_mendes = Candidato(
    'Ana Carolina Mendes',
    '@ana_mendes_rj',
    41,
    'PSP (Partido Socialista do Povo)',
    'Doutora em Ciências Sociais',
    'Professora universitária',
    'Ana Carolina Mendes é uma intelectual de renome, professora universitária e ativista social, conhecida por seu trabalho de pesquisa sobre desigualdade urbana e direito à cidade. Com um forte interesse por eventos culturais e pela preservação do patrimônio histórico do Rio de Janeiro, Ana busca promover uma política de geração de emprego ligada ao setor cultural e de turismo. Sua plataforma foca em expandir a assistência social, fortalecer o SUS e garantir uma gestão transparente das contas públicas, com ênfase na redução de desigualdades.',
    './resources/ana-carolina-mendes.txt'
)

fernando_costa = Candidato(
    'Fernando Costa Lima',
    '@fernando_costa',
    44,
    'PDL (Partido Democracia e Liberdade)',
    'Graduado em Administração',
    'Empresário do setor de eventos',
    'Fernando Costa Lima é um empresário do setor de eventos, com uma forte ligação com o carnaval carioca. Ele acredita que a cultura é uma ferramenta essencial para o desenvolvimento econômico e social da cidade. Sua campanha foca no combate à corrupção, reforçando a necessidade de transparência nas obras públicas, além de priorizar a segurança nas comunidades e garantir acesso à saúde de qualidade. Fernando é casado e valoriza a família como pilar fundamental da sociedade.',
    './resources/fernando-costa-lima.txt'
)

luciana_souza = Candidato(
    'Luciana Souza',
    '@luci_sou',
    28,
    'PMC (Partido do Movimento Comunista)',
    'Graduada em Serviço Social',
    'Assistente social',
    'Luciana Souza é assistente social e uma apaixonada por viagens que ampliam seu entendimento sobre diferentes culturas. Sua campanha busca melhorar a assistência social, saúde e saneamento nas comunidades mais carentes do Rio. Ana é praticante de umbanda e acredita que a espiritualidade e a diversidade são fundamentais para a construção de uma sociedade mais justa. Ela defende investimentos em educação como forma de empoderar as comunidades e garantir um futuro melhor.',
    './resources/luciana-souza.txt'
)

# iniciando a função da nuvem de palavras
jorge_ribeiro.create_wordcloud()
ana_mendes.create_wordcloud()
fernando_costa.create_wordcloud()
luciana_souza.create_wordcloud()
