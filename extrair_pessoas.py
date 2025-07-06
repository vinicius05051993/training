import spacy
import json
import sys

def extrair_dados(texto):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(texto)
    pessoas = set(ent.text for ent in doc.ents if ent.label_ == "LOC")
    return {"Locais": list(pessoas)}

if __name__ == "__main__":
    texto = """A confeiteira Lexandra Machado estava no quintal de casa quando viu uma montanha de 80 metros de altura deslizando a poucos quilômetros, na manhã de 7 de dezembro de 2024, no povoado de Casquilho de Cima, em Conceição do Pará (MG). O que ela via era o rompimento de uma pilha de rejeitos de uma mineradora.

             “Fiquei tão atordoada, que comecei a gritar. Logo me lembrei de Brumadinho. Após uns 40 minutos, os funcionários da empresa passaram de carro, dizendo que era para sairmos de casa”, conta Lexandra.
             As pilhas de rejeito têm sido utilizadas pelas mineradoras como uma alternativa mais segura às barragens a montante, que foram proibidas no Brasil após a morte de quase 300 pessoas nas cidades de Brumadinho e Mariana, em 2015 e 2019.

             Entenda a diferença entre barragens, pilhas de rejeito e pilhas de estéril
             Embora tenham menor potencial de dano, ainda não há regulamentação federal e protocolo de fiscalização, o que também torna as pilhas de rejeitos um risco, segundo especialistas. O governo federal prevê definir regras para a prática até 2026.

             O deslizamento em Conceição do Pará atingiu 7 casas e, quatro meses depois, nenhum morador pôde voltar ao povoado. Essa foi a quarta ocorrência envolvendo pilhas desde 2018. Em um dos casos, no município de Godofredo Viana, no Maranhão, uma rodovia ficou interditada por seis dias.

             Mais pilhas do que barragens
             Desde 2019, as barragens do tipo a montante -- estruturas nas quais os rejeitos da mineração são depositados em camadas sucessivas -- são proibidas no Brasil, por que estão mais suscetíveis a acidentes.

             A mudança na legislação ocorreu após os rompimentos em Mariana e Brumadinho. A partir de então, a disposição dos resíduos em pilhas passou a dominar o setor de mineração, de acordo com o Conselho Regional de Engenharia e Agronomia de Minas Gerais.

             Dados da Vale, a maior mineradora do país e responsável pelas barragens que romperam em Minas Gerais, mostram que houve aumento no número de pilhas de rejeito. Hoje, 70% dos rejeitos da mineradora estão armazenados em pilhas e não em barragens. Esse número era de 40% em 2014.

             Já a Samarco, outra responsável pelo rompimento da barragem em Mariana, filtra e empilha atualmente cerca de 80% dos rejeitos de minério que produz, uma mudança que vem sendo feita desde 2020.

             As pilhas são como montanhas de lixo da mineração, formadas pelo material sem valor econômico que resta após a lavagem do minério e a drenagem da água. Já nas barragens, o rejeito é armazenado com água, formando uma espécie de lama. Há, ainda, as pilhas de estéril, formadas principalmente pela areia retirada do solo até se chegar ao minério.

             De acordo com especialistas ouvidos pelo g1, algumas pilhas que foram licenciadas -- ou que estão em processo de licenciamento no Brasil -- poderão alcançar mais de 200 metros de altura, o que eles consideram um grande risco, principalmente porque essas estruturas não são regulamentadas ou monitoradas como as barragens passaram a ser depois das tragédias em Minas Gerais.

             De acordo com o engenheiro Júlio Grillo, ex-superintendente do Ibama de MG, o material seco que é depositado nas pilhas tende a se acomodar mais rapidamente e alcança uma área menor do que a lama, em caso de rompimento. Por isso, o potencial de dano é menor. No entanto, a falta de fiscalização e de transparência quanto aos cálculos que definem as dimensões das pilhas preocupam.

             “Isso faz com que a probabilidade de rompimento de uma pilha, hoje, seja maior do que a de uma barragem, que já tem regulamentações e critérios de licenciamento mais rigorosos”, disse o engenheiro.
             Na Agência Nacional de Mineração (ANM), órgão do governo federal responsável pela gestão de mineradoras, o assunto só entrou na agenda regulatória para o biênio de 2025 e 2026, o que significa que a pauta só vai começar a ser discutida neste ano.

             Júlio Nery, diretor de assuntos minerários do Instituto Brasileiro de Mineração (Ibram), entidade que representa as mineradoras, afirma que o setor já segue o Padrão Global da Indústria para Gerenciamento de Rejeitos, o que inclui o empilhamento a seco.

             ANM não tem cronograma de vistorias
             Em 2024, técnicos da ANM vistoriaram 180 barragens, de acordo com o relatório anual do órgão. Esse é um dado que não existe em relação às pilhas, porque não há um cronograma de vistorias, nem “uma equipe dedicada exclusivamente para essa fiscalização”, segundo a agência.

             Também não existe “um cadastro que permita rastrear a quantidade de vistorias específicas de pilhas”. Segundo a agência, as pilhas de rejeitos são vistoriadas “junto às ações rotineiras”.

             Enquanto a lei 12.334, de 2010, criou a Política Nacional de Segurança de Barragens, com critérios para monitoramento, normas de controle e padrão de segurança, nada disso existe em relação às pilhas.

             Além disso, informações técnicas sobre as barragens estão disponíveis em bancos de dados públicos, como o Sistema Integrado de Gestão de Barragens de Mineração. Já informações sobre as condições estruturais das pilhas e os critérios para que sejam licenciadas não existem.

             De acordo com o engenheiro Júlio Grillo, faltam dados importantes sobre o cálculo para o preparo da base das pilhas e para definir a altura máxima que essas estruturas podem ter.

             “A pilha rompeu em Conceição do Pará, porque a base não foi preparada adequadamente para aguentar o peso”, disse o especialista, sobre o deslizamento na mineradora Jaguar Mining, que Lexandra observou de dentro de casa.

             A pilha no povoado tem, atualmente, 80 metros de altura. Isso é mais que o dobro do Cristo Redentor, que tem 35 metros. A área é de aproximadamente 16 hectares, quase o tamanho do estádio Maracanã, que tem 18 hectares. De acordo com a última informação repassada pela Jaguar Mining para a ANM, o desabamento movimentou um volume de cerca de 640 milhões de litros.

             Questionada sobre qual a altura e as demais medidas que foram autorizadas no projeto de licenciamento da pilha, a Jaguar Mining respondeu que a estrutura “não tinha atingido sua altura e volume máximos e operava de acordo com licenciamento junto aos órgãos reguladores”.

             A Secretaria de Estado de Meio Ambiente e Desenvolvimento Sustentável (Semad), de Minas Gerais, informou que “os aspectos geotécnicos das pilhas extrapolam o escopo do licenciamento ambiental” e que a ANM é a responsável por essa análise técnica.

             Já a agência federal disse que a licença de operação “é de responsabilidade do órgão ambiental”, no caso, a própria Semad, e que vinha sendo renovada automaticamente desde 2012. A ANM informou que vistoriou a pilha nove vezes desde 2009, sendo a última em 2021. Nessas ocasiões, "ocorreram publicação de exigências, autuações, interdições parciais relativas a diversos aspectos do empreendimento".

             Mineradoras dizem seguir padrão internacional
             Segundo relatório anual exigido das mineradoras pelo código de mineração, o país tem mais de 3 mil pilhas de rejeito, estéril ou mistas.

             Dessas, 232 são apenas de rejeitos, sendo 41 da mineração de ferro -- que produz as pilhas mais altas -- e de ouro, que tem as substâncias mais tóxicas, como arsênio, cianeto e mercúrio.


             Para Carlos Bruno Ferreira, procurador do Ministério Público Federal em Minas Gerais, as mineradoras estão apostando nas pilhas de rejeito não apenas por ser uma estrutura com menor potencial de risco, mas também porque falta regulação.

             “A partir do momento que o minerador não tem obrigações para cumprir, que pode deixar a pilha sem equipamentos que verifiquem a solidez da estrutura, sem o equipamento de vídeo e sem uma equipe de segurança, como eu verifiquei no caso da Jaguar Mining, se torna mais simples colocar os rejeitos em forma de pilha”, disse.
             Segundo o diretor do Ibram, Júlio Nery, a entidade é responsável por duas normas técnicas que tratam dos parâmetros para a construção das pilhas de estéril e barragens. Elas funcionam como recomendações definidas pelo próprio setor e não têm força de lei.

             De acordo com essas normas, o projeto para instalação de uma pilha de rejeito deve incluir, entre outras coisas, plano de monitoramento e inspeções, estudos sobre grau de risco e um plano de ação de emergência. “Elas existem desde a década de 1990 e são periodicamente revisadas”, afirma o engenheiro.

             O diretor do Ibram afirmou ainda que as dimensões das pilhas “podem variar em função da topografia, dos locais de disposição, da geologia local e a localização geográfica”.

             Ao menos quatro deslizamentos desde 2018
             A deputada federal Duda Salabert (PDT-MG) mapeou quatro ocorrências com pilhas de rejeito ou de estéril em seis anos. Ela é autora de um projeto de lei que pretende regulamentar aspectos de segurança para as pilhas de mineração.

             A proposta está na Comissão de Meio Ambiente da Câmara dos Deputados desde novembro de 2024, à espera de um relator.

             O caso mais grave e recente foi o de Conceição do Pará, em Minas Gerais. Sete casas foram atingidas e cerca de 250 pessoas tiveram que ser realocadas. Nenhum morador pode voltar ao povoado, mais de quatro meses depois do acidente.

             Um acordo entre a Jaguar Mining, a Defensoria Pública de Minas Gerais e o Ministério Público Federal foi assinado em março de 2025 e define os termos para indenizações. Alguns moradores poderão voltar a suas casas, mas ainda não foi concluída a delimitação da área de segurança.

             Em nota, a Jaguar MIning disse que tem prestado todas as informações aos órgãos fiscalizadores e regulatórios para o esclarecimento das causas da ruptura parcial da pilha".

             O primeiro caso de deslizamento foi em 2018, na cidade de Godofredo Viana (MA). A pilha de estéril da mineradora de ouro Aurizona deslizou, bloqueando a única via de acesso e deixando uma comunidade isolada. Cinco anos depois, em 2023, outro deslizamento aconteceu na mesma região. A estrada ficou interditada por seis dias.

             Já em 2022, uma erosão na pilha de rejeitos da mineradora AngloGold Ashanti, assustou moradores de Santa Bárbara (MG). A empresa confirmou que o problema foi causado pelas fortes chuvas no período.

             Riscos com a chuva
             Segundo o engenheiro Euler Cruz, presidente do Fórum Permanente São Francisco, uma entidade da sociedade civil que se dedica à segurança e à qualidade de vida da população que vive em áreas de mineração em Minas Gerais, o empilhamento a seco é um tipo de tecnologia que não está totalmente dominado.

             As estruturas, segundo o engenheiro, não estão sendo planejadas para suportar o maior volume de chuvas, devido às mudanças climáticas. “Os sistemas de drenagem são projetados com dados pluviométricos de 40 ou 50 anos atrás. Não se leva em conta as chuvas torrenciais que vemos agora”.

             O engenheiro Júlio Grillo concorda: “As pilhas não vão provocar desastres tão grandes como o rompimento de uma barragem, mas, certamente, vão sucumbir às chuvas fortes mais rapidamente”, disse.

             Para evitar novos e mais graves acidentes, Grillo aponta três caminhos:

             O processo de licenciamento não pode ser baseado em autodeclarações;
             Qualquer empreendimento minerário tem que estar comprovadamente adequado aos eventos extremos de chuva;
             É preciso aplicar o princípio da precaução e da prevenção. As mineradoras têm que comprovar de forma transparente que a pilha a ser licenciada é sustentável a longo prazo."""

    print("Uso: python extrair_dados.py '"+ texto +"'")
    resultado = extrair_dados(texto)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))