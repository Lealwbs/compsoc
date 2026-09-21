# -*- coding: utf-8 -*-
"""
Discussão 1
Aluno: Italo Leal Lana Santos
Matrícula: 2024013893
"""

import os
from fpdf import FPDF

class ClassicPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(20, 20, 20)
        self.set_auto_page_break(auto=True, margin=18)
        
        # Fontes clássicas (Times New Roman)
        self.add_font('TimesNewRoman', '', r'C:\Windows\Fonts\times.ttf')
        self.add_font('TimesNewRoman', 'B', r'C:\Windows\Fonts\timesbd.ttf')
        self.add_font('TimesNewRoman', 'I', r'C:\Windows\Fonts\timesi.ttf')

    def footer(self):
        self.set_y(-12)
        self.set_font('TimesNewRoman', 'I', 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f'{self.page_no()}', align='C')

    def add_title_block(self, title, student_name, matricula):
        self.set_font('TimesNewRoman', 'B', 14)
        self.set_text_color(0, 0, 0)
        self.cell(0, 7, title, align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('TimesNewRoman', '', 11)
        self.cell(0, 6, f"Aluno: {student_name}", align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(0, 6, f"Matrícula: {matricula}", align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(5)

    def add_qa(self, number, question, answer):
        self.set_font('TimesNewRoman', 'B', 10.5)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5.1, f"{number}. {question}")
        self.ln(0.8)
        self.set_font('TimesNewRoman', '', 10.5)
        self.multi_cell(0, 5.1, answer, align='J')
        self.ln(3.2)

def build_pdf():
    pdf = ClassicPDF()
    pdf.add_page()
    
    pdf.add_title_block(
        "Discussão 1",
        "Italo Leal Lana Santos",
        "2024013893"
    )
    
    perguntas_respostas = [
        (
            1,
            "O que significa \"bem-estar\"?",
            "Olha, para mim, bem-estar quando a gente fala de rede social é uma coisa bem simples de sentir, mas meio chata de explicar: é basicamente você fechar o aplicativo e não bater aquele arrependimento imediato de ter jogado seu tempo no lixo. Digo isso porque hoje em dia a gente abre o celular rapidinho e, quando assusta, já se passaram duas horas vendo vídeos nada a ver, ficando com a cabeça pesada, se comparando com a vida perfeita dos outros ou perdendo o sono de bobeira. Então, na minha visão, bem-estar é quando o aplicativo realmente agrega alguma coisa na sua rotina, te diverte de verdade ou te aproxima de quem você gosta, sem sugar sua atenção de forma predatória e sem te deixar ansioso ou esgotado no final."
        ),
        (
            2,
            "Como transformar bem-estar em uma variável mensurável?",
            "Essa é uma pergunta complicada porque sentimentos não são números exatos que a gente joga numa tabela e pronto. Curtida e tempo de tela são fáceis de medir no sistema, mas bem-estar é subjetivo demais. Eu acho que, em vez de focar só em minutos conectado, a plataforma deveria observar outros comportamentos que mostram se a relação do usuário com o app é saudável ou não. Por exemplo, ver se a pessoa consegue fechar o aplicativo numa boa sem ficar reabrindo de minuto em minuto por pura compulsão, se ela não fica usando até altas horas da madrugada e até fazer perguntas diretas e rápidas de vez em quando, tipo perguntar se aquela sessão foi útil. Acaba que o melhor sinal de que a pessoa está bem é justamente ela não depender do app o tempo todo."
        ),
        (
            3,
            "Quem deve definir o que é bem-estar?",
            "Sinceramente, acho que essa é uma daquelas coisas que não dá para deixar na mão de um grupo só decidir. Se a gente deixar a própria empresa definir, é óbvio que ela vai puxar a sardinha para o lado do lucro e inventar que bem-estar é você passar cinco horas vendo anúncios e interagindo com tudo. Por outro lado, se o governo quiser ditar sozinho o que é bom para a cabeça do cidadão, a gente entra num terreno perigoso de controle moral e censura que ninguém quer. Para mim, teria que ser uma mistura: especialistas em psicologia e saúde mental ajudam a definir regras básicas de segurança, a lei garante proteções gerais e o próprio usuário tem que ter autonomia para configurar o que faz sentido para ele, afinal cada um sabe onde o calo aperta."
        ),
        (
            4,
            "Como obter os dados necessários para medir bem-estar?",
            "Para ser bem sincero, aqui mora um perigo gigantesco de virar uma invasão de privacidade sem tamanho. Eu acho péssimo pensar em um aplicativo ficando de olho na minha câmera para ver se eu estou sorrindo, monitorando minhas mensagens no privado ou analisando meu tom de voz para saber se estou triste ou estressado. Isso parece coisa de filme de distopia. O caminho mais justo, na minha opinião, é trabalhar com dados anônimos processados no próprio aparelho da pessoa, sem ficar mandando tudo para o servidor da empresa, além de coletar opiniões voluntárias em pesquisas rápidas de satisfação. O sistema tem que ser projetado para ser saudável por natureza, sem precisar espionar a nossa vida íntima."
        ),
        (
            5,
            "Bem-estar imediato ou de longo prazo?",
            "Com certeza absoluta deveria focar no longo prazo. O grande problema das redes sociais atuais é que elas foram desenhadas justamente para explorar o prazer imediato, aquela dopamina rápida que você ganha vendo uma fofoca, uma treta nos comentários ou um vídeo idiota qualquer. Na hora parece legal e você fica preso ali, mas dali a meia hora você percebe que não ganhou nada com aquilo e fica com uma sensação horrível de tempo perdido. Se a ideia for realmente melhorar a vida das pessoas, o algoritmo precisa priorizar coisas que continuem fazendo sentido depois, incentivando conteúdos que agreguem conhecimento ou conexões reais, em vez de ficar viciando o cérebro em recompensas instantâneas que só geram vazio."
        ),
        (
            6,
            "Como o próprio usuário pode saber o que maximiza seu bem-estar?",
            "A verdade nua e crua é que a gente quase nunca sabe o que é melhor para nós quando estamos no piloto automático rolando o feed. Eu mesmo perco as contas de quantas vezes cliquei em uma postagem só por curiosidade boba e depois me arrependi na mesma hora. Então, clicar em algo não significa nem de longe que aquilo me fez bem. Para que o usuário consiga entender o que realmente melhora o seu bem-estar, a plataforma teria que quebrar esse transe, talvez mostrando de forma bem clara relatórios semanais de onde foi parar o tempo dele ou pedindo uma avaliação dos temas depois que a poeira baixa, para a gente conseguir separar o impulso do momento daquilo que realmente importa."
        ),
        (
            7,
            "Devemos personalizar a definição de bem-estar?",
            "Acho que tem que ter um meio-termo aí. Por um lado, existem coisas que são universais para qualquer ser humano: todo mundo precisa dormir bem, ninguém gosta de sofrer linchamento virtual e qualquer incentivo à automutilação ou ódio faz mal para qualquer pessoa; então esse básico tem que ser igual para todo mundo e pronto. Mas, fora isso, cada pessoa é um universo diferente. Para mim, bem-estar pode ser ficar vendo conteúdos de programação, futebol e memes leves, enquanto para outra pessoa pode ser acompanhar notícias de economia ou arte. O segredo é deixar a própria pessoa escolher suas preferências conscientemente, e não o algoritmo ficar tentando adivinhar e manipular nossos gostos por baixo dos panos."
        ),
        (
            8,
            "O algoritmo deveria às vezes recomendar algo que o usuário não escolheria?",
            "Eu acho que sim, mas tem que ser com muito cuidado e sem forçar a barra. Se o algoritmo só entregar exatamente o que eu já consumo todo santo dia, eu acabo ficando preso numa bolha terrível, achando que o mundo inteiro pensa igual a mim e ficando intolerante com qualquer opinião contrária. De vez em quando, receber a indicação de um assunto diferente, um ponto de vista bem fundamentado que contradiga o meu ou algo culturalmente novo ajuda bastante a abrir a cabeça. O que a plataforma não pode fazer é empurrar absurdos ou polêmicas só para me irritar e me fazer brigar nos comentários, que é o que muita rede faz hoje para gerar engajamento."
        ),
        (
            9,
            "Como evitar a \"Lei de Goodhart\"?",
            "Essa lei acontece o tempo todo e é super fácil de entender: se a plataforma pegar o bem-estar e transformar isso numa nota simples de 1 a 5, rapidinho as pessoas e o próprio sistema vão dar um jeito de burlar a regra. Os criadores de conteúdo vão começar a gravar vídeos com lições de moral forçadas, fazer chantagem emocional ou pedir para os seguidores darem cinco estrelas para ganhar sorteios, e no fim a nota vai ser alta sem ninguém estar realmente melhor. Para fugir dessa armadilha, a rede não pode depender de um número único. É preciso cruzar vários sinais diferentes ao longo do tempo, mudar a forma de medição com frequência e nunca vincular pagamentos diretamente a essas notas de avaliação."
        ),
        (
            10,
            "Como avaliar causalidade?",
            "É muito fácil confundir as coisas e achar que uma coisa causou a outra só porque elas aconteceram juntas. Por exemplo, se uma pessoa passa o dia inteiro no celular e está deprimida, pode ser que a rede social tenha deixado ela mal, mas também pode ser que ela já estivesse passando por problemas pesados na família, no trabalho ou na faculdade e foi para o celular justamente para tentar fugir da realidade. Para comprovar se o algoritmo é realmente o culpado, não dá para ficar só na correlação. Teria que ser feito um estudo sério acompanhando as pessoas ao longo de meses, comparando quem usa versões diferentes do aplicativo e levando em consideração a rotina real de cada um fora da internet."
        ),
        (
            11,
            "Como realizar experimentos de forma ética?",
            "Olha, para mim a regra básica é que as pessoas nunca deveriam ser usadas como cobaias de coisas que podem machucar a cabeça delas. Aquele caso do Facebook em 2014, que manipulou o feed de uma galera de propósito para ver se elas ficavam mais tristes, foi um absurdo sem tamanho. Qualquer teste precisa ser feito para tentar melhorar a vida do usuário, e não para descobrir até onde vai a resistência emocional dele. E quando a gente fala de crianças e adolescentes, aí é que não deveria ter experimento nenhum mesmo: com esse público a postura tem que ser de proteção máxima o tempo todo, sem ficar inventando moda de teste psicológico no feed."
        ),
        (
            12,
            "Como tratar objetivos conflitantes?",
            "Esse é o maior nó da questão, porque a gente sabe que na prática os interesses batem de frente: a empresa quer faturar, o usuário quer paz e conteúdo relevante, e a sociedade quer segurança. Se tentar colocar tudo no mesmo saco, a busca por lucro sempre vai passar por cima da saúde mental. Na minha cabeça, a saída é definir prioridades claras: proteção, privacidade e segurança não podem entrar em negociação e têm que ser o ponto de partida obrigatório exigido por lei. O resto das coisas, como escolher entre ver mais novidades ou manter um feed mais calmo e focado, deveria ser decidido pelo próprio usuário nas configurações, sem segredos."
        ),
        (
            13,
            "O que acontece com o modelo de negócio?",
            "Sendo bem realista, o modelo de negócios atual, que vive de prender o olho da pessoa na tela para empurrar anúncio goela abaixo, simplesmente morre numa rede focada em bem-estar. Se o objetivo passa a ser você usar menos o celular, a quantidade de visualizações de propagandas vai despencar. Então a empresa teria que se reinventar: ela poderia adotar um modelo de assinatura barata para quem quer uma rede limpa e sem anúncios, cobrar pequenas comissões sobre transações e serviços reais contratados na plataforma, ou cobrar mais caro de marcas sérias que queiram anunciar para um público atento e tranquilo, em vez de bombardear usuários distraídos que nem prestam atenção."
        ),
        (
            14,
            "Como saber se a plataforma realmente está otimizando bem-estar?",
            "Não dá para ser ingênuo e acreditar no que a própria empresa fala. Se depender do marketing deles, todas as redes sociais são lugares maravilhosos que só querem espalhar amor pelo mundo, enquanto os relatórios internos mostram o contrário. A única forma de a gente ter certeza de verdade é com auditoria externa e independente. Teria que ter gente de fora, como pesquisadores de universidades e órgãos da sociedade civil, com acesso direto aos dados e aos algoritmos para auditar o que está acontecendo de fato. Sem essa transparência real para quem estuda o assunto, qualquer papo de bem-estar vira só jogada de relações públicas para acalmar a justiça."
        ),
        (
            15,
            "O algoritmo deveria ser diferente para crianças, adolescentes e adultos?",
            "Com toda certeza do mundo. Quem é mais jovem ainda está com a cabeça em formação, é muito mais inseguro e sente uma necessidade absurda de ser aceito pelos colegas da escola e da internet. Tratar um menino de doze anos com o mesmo algoritmo agressivo feito para um adulto de trinta é de uma irresponsabilidade bizarra. Para os jovens, a rede já deveria vir bloqueada por padrão contra mecanismos viciantes: sem rolagem infinita, sem reprodução automática de vídeos, sem mandar notificações de madrugada para não estragar o sono e sem mostrar número de curtidas e seguidores, para evitar que vire uma disputa doentia de popularidade."
        ),
        (
            16,
            "Quem é responsável quando a otimização produz consequências indesejadas?",
            "Para mim, a conta maior tem que ir para a diretoria e os executivos da empresa, porque são eles que batem o martelo nas metas de faturamento e mandam implementar algoritmos agressivos sabendo dos riscos. Mas a gente que programa, como futuros cientistas da computação e desenvolvedores, também não pode fingir de desentendido e colocar a culpa só no sistema. Se você está criando uma funcionalidade e vê claramente que aquilo vai incentivar desafios perigosos ou fazer mal para os outros, você tem a obrigação moral de falar e se recusar a fazer. Todo mundo envolvido tem sua parcela de responsabilidade, tanto legal quanto ética."
        ),
        (
            17,
            "Quem deveria regular a função objetivo?",
            "A história já provou por A mais B que confiar que a própria empresa vai se autorregular é pedir para ser enganado, porque quando o lucro aperta, a ética vai para o ralo. Por outro lado, deixar o governo controlar a dedo o algoritmo também é um perigo danado, porque rapidinho alguém usa isso para perseguir adversários políticos e censurar o que não gosta. O caminho mais sensato, a meu ver, é criar regras gerais por lei que obriguem as plataformas a terem responsabilidade com a segurança das pessoas, com conselhos independentes e multissetoriais fiscalizando se o serviço não está causando danos sociais, sem precisar ficar dizendo exatamente qual código programar."
        ),
        (
            18,
            "É possível provar que um algoritmo \"maximiza o bem-estar\"?",
            "Provar matematicamente no papel, tipo uma fórmula exata de física, é impossível, porque o bem-estar humano muda todo dia e cada pessoa reage de um jeito dependendo do que está vivendo fora da tela. Mas demonstrar na prática através de dados e estudos de longo prazo é totalmente viável. A gente consegue acompanhar grupos de pessoas e verificar se, com um algoritmo mais saudável, elas relatam menos ansiedade, dormem melhor, perdem menos tempo com coisas inúteis e se sentem mais dispostas no dia a dia. Pode não ser uma prova matemática infalível, mas são evidências reais e práticas que mostram se a mudança fez bem ou não."
        ),
        (
            19,
            "Como conciliar bem-estar do usuário e modelo de negócio dessa plataforma?",
            "Essa conciliação só funciona se a empresa parar com essa mania de querer bater recorde de lucro a cada três meses e começar a pensar no longo prazo. Uma rede que destrói a saúde mental dos usuários cria uma imagem horrível, afasta as famílias e acaba tomando processos judiciais bilionários como esse recente da Meta. Quando a plataforma trata o usuário com respeito e ajuda a vida dele a ser melhor, ela constrói uma relação de confiança duradoura. As pessoas ficam felizes de continuar ali por anos e até aceitam pagar por serviços que agreguem valor de verdade. No fim das contas, cuidar do cliente também é um modelo de negócios sustentável."
        ),
        (
            20,
            "Qual é a proposta de valor dessa rede social?",
            "A proposta de valor teria que ser muito sincera: 'Uma rede social que te conecta de verdade ao que interessa, no menor tempo de tela possível, para você viver melhor a sua vida real'. A grande sacada dela em comparação com redes como o TikTok ou o Instagram seria justamente não tentar te sequestrar. O foco não seria te prender na cama até de madrugada rolando vídeos no automático, mas sim te ajudar a falar com quem você gosta, se informar com qualidade ou aprender algo útil, e logo em seguida te devolver para o seu dia com a cabeça leve e a sensação de tempo bem aproveitado."
        ),
        (
            21,
            "Se o sucesso de uma rede social deixar de ser medido por \"quanto tempo consegue manter o usuário\" e passar a ser medido por \"quanto valor proporciona ao usuário\", como deveria mudar o produto, o marketing e o modelo de negócio dessa empresa? Como pensar fora da caixa?",
            "A mudança teria que ser total em todas as frentes. No produto, o aplicativo teria um ponto final bem claro no feed, te avisando que você já viu o que precisava e sugerindo fechar o celular para ir viver sua vida, além de focar em resumos inteligentes em vez de rolagem infinita. No marketing, a empresa venderia paz de espírito, foco e equilíbrio, atraindo todo mundo que já está de saco cheio da ansiedade das redes convencionais. O dinheiro viria de assinaturas acessíveis ou de ferramentas úteis para trabalho e estudo. E pensando bem fora da caixa, o ideal seria que a rede funcionasse como um protocolo aberto, onde o próprio usuário pudesse escolher o algoritmo de recomendação que preferir em uma espécie de catálogo livre, tirando o monopólio das mãos de uma única empresa."
        )
    ]
    
    for num, q, a in perguntas_respostas:
        pdf.add_qa(num, q, a)
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'discussao_1_respostas.pdf')
    pdf.output(output_path)
    print(f"Sucesso: {output_path}")

if __name__ == '__main__':
    build_pdf()
