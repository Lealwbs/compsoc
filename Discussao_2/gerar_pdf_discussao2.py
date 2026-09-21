# -*- coding: utf-8 -*-
"""
Discussão 2
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
        self.multi_cell(0, 5.2, f"{number}. {question}")
        self.ln(0.8)
        self.set_font('TimesNewRoman', '', 10.5)
        self.multi_cell(0, 5.2, answer, align='J')
        self.ln(3.5)

def build_pdf():
    pdf = ClassicPDF()
    pdf.add_page()
    
    pdf.add_title_block(
        "Discussão 2",
        "Italo Leal Lana Santos",
        "2024013893"
    )
    
    perguntas_respostas = [
        (
            1,
            "Qual é a importância de criar ferramentas para acompanhar representantes no Parlamento?",
            "Para ser bem sincero, na minha visão o maior problema da nossa política hoje em dia é que o eleitor vota e, dois ou três meses depois, já esqueceu completamente o nome do deputado ou vereador em quem votou. Acaba que os políticos ficam quatro anos praticamente soltos, sem nenhuma cobrança do povo, e só voltam a fingir serviço perto da próxima eleição. O Brasil tem uma quantidade absurda de dados públicos abertos no TSE, na Câmara e no Senado, mas esses dados são muito espalhados, cheios de termos complicados e ninguém tem paciência de ficar caçando ata de votação em PDF. Então uma plataforma simples e direta é fundamental para refrescar a memória da galera, traduzir essas informações difíceis para o dia a dia e ainda explicar como funciona o tal do quociente eleitoral, mostrando para onde vai de verdade o nosso voto."
        ),
        (
            2,
            "Como a plataforma deve tratar candidatos que estão tentando a reeleição ao mesmo cargo?",
            "Para quem já está com mandato e quer se reeleger, a ferramenta tem que agir como uma verdadeira prestação de contas do que o cara fez nos últimos quatro anos, sem cair na conversa mole do horário eleitoral. A plataforma precisa mostrar o que ele produziu de verdade: quais projetos de lei relevantes ele apresentou (separando o que é lei importante de projetos bobos de dar nome a rua ou homenagens), como ele votou nas matérias pesadas que afetam o nosso bolso, se ele realmente comparecia nas sessões e, principalmente, como ele gastou a cota parlamentar e a verba de gabinete. O eleitor precisa bater o olho e ver se aquele político trabalhou pelo povo ou se só aproveitou o cargo para curtir mordomias com dinheiro público."
        ),
        (
            3,
            "Como analisar candidatos que já ocupam cargo público e concorrem a um cargo diferente?",
            "Quando o político já tem um cargo e tenta pular para outro, tipo um vereador querendo virar deputado federal ou um deputado tentando a prefeitura, o aplicativo tem que analisar se a trajetória dele faz sentido para essa nova função e se há coerência no que ele defende. Outro ponto crucial que a gente tem que ficar muito atento é o envio de emendas parlamentares. É batata: muitas vezes o parlamentar começa a mandar uma montanha de dinheiro de emenda justamente para as cidades onde ele quer cavar votos para a nova eleição. O sistema tem que jogar luz sobre isso e mostrar se o candidato tem propostas de verdade ou se só está usando o cargo atual de trampolim eleitoreiro."
        ),
        (
            4,
            "Como a plataforma deve tratar candidatos que não ocupam cargo público no momento?",
            "Aqui a gente tem duas situações bem diferentes que não podem ser misturadas: quem está estreando na política e quem já foi político no passado e quer voltar. Para quem nunca teve mandato, o foco tem que ser na vida dele fora da política: qual é a formação, no que trabalhou, como evoluiu o patrimônio declarado no TSE, quem está doando dinheiro para a campanha e se as propostas dele batem com o que o partido prega. Já para quem está tentando voltar depois de uns anos fora, a plataforma tem uma obrigação sagrada de combater a nossa amnésia: resgatar o histórico antigo do TSE desde 2004, puxar como ele votava no passado, se teve contas rejeitadas pelo Tribunal de Contas ou se responde a processos, para não deixar político velho posar de novidade no pedaço."
        ),
        (
            5,
            "Como deve funcionar o acompanhamento no período pré-eleitoral (antes das eleições)?",
            "Nos anos normais em que não tem eleição, a plataforma tem que servir para manter o cidadão acordado e informado, criando uma cultura de vigilância contínua. Ela precisa disponibilizar uma linha do tempo clara da carreira do político, mostrando trocas de partido e votos polêmicos. Uma função que eu acho que seria muito massa é o módulo \"Fala versus Voto\": o sistema pega o que o deputado posta nos vídeos do Instagram ou no Twitter e compara na lata com o voto dele registrado na Câmara. Se o cara vive fazendo discurso de que ama a educação ou a saúde, mas na hora da votação votou pelo corte de verbas dessas áreas, o aplicativo avisa o usuário sobre a contradição, escancarando a hipocrisia na hora."
        ),
        (
            6,
            "Como a plataforma deve apoiar o eleitor durante o período eleitoral (na escolha do voto)?",
            "Durante as semanas de campanha, o aplicativo tem que ser o melhor amigo do eleitor indeciso. A ideia principal seria um sistema de \"Match Eleitoral\": o cidadão responde a umas perguntas simples sobre assuntos importantes do dia a dia (tipo impostos, segurança, meio ambiente e saúde) e o sistema calcula quais candidatos mais pensam parecido com ele. Só que, ao contrário dos testes que a gente vê por aí onde o próprio candidato responde o que quiser para parecer bonzinho, o nosso cálculo tem que ser baseado no histórico real de votações do político. Além disso, tem que ter um simulador visual bem didático ensinando como funciona o quociente eleitoral, para a pessoa entender que votar no candidato famoso pode acabar elegendo outro cara do partido que ela nem conhece."
        ),
        (
            7,
            "Como deve ser o acompanhamento no período pós-eleitoral (depois das eleições)?",
            "Depois que passa a eleição e o candidato toma posse, o trabalho do sistema não pode parar de jeito nenhum. A plataforma permitiria ao usuário cadastrar os representantes em quem ele votou para receber alertas automáticos no celular, avisando quando o deputado votou em alguma matéria importante ou quando lançou gastos altos na cota parlamentar. Outra ideia muito útil é um rastreador de promessas de campanha, que pega as propostas registradas oficialmente no TSE e acompanha se o político está correndo atrás delas ou se esqueceu de tudo. Por fim, dá para cruzar no mapa para onde o parlamentar mandou o dinheiro das emendas com os dados de carência do IBGE, para ver se ele ajudou quem precisava ou se foi só toma lá dá cá."
        ),
        (
            8,
            "Como implementar a verificação de notícias e discursos (fact-checking) de forma funcional?",
            "Para checar o que os candidatos falam em debates, entrevistas e redes sociais, a plataforma precisa de uma esteira bem prática. Primeiro, transcrevemos os vídeos de debates e usamos processamento de texto para separar o que é opinião pessoal (que não dá para checar) daquilo que é afirmação com dados concretos, tipo o cara dizer que votou contra um imposto ou que repassou tantos milhões para uma cidade. A partir daí, o sistema busca automaticamente nos dados oficiais do governo (Câmara, TSE, IBGE e Transparência) para confirmar se o dado é real ou mentira. O resultado tem que ser publicado de forma muito clara, com selos diretos como \"Verdadeiro\", \"Falso\" ou \"Contraditório\", sempre colocando o link da fonte oficial para o próprio cidadão poder conferir com os próprios olhos."
        ),
        (
            9,
            "Quais técnicas de engenharia de dados e integração devem ser adotadas?",
            "Para a coisa toda funcionar sem travar, a parte de engenharia de dados tem que ser muito bem estruturada. A plataforma precisa consumir automaticamente as APIs abertas da Câmara dos Deputados e do Senado todos os dias para puxar projetos, votações e notas fiscais. O problema maior são as Assembleias dos estados e as Câmaras de vereadores, que muitas vezes não têm APIs decentes, então a gente vai precisar criar robôs de raspagem de dados (web scraping) e leitores de PDF para extrair informações dos diários oficiais. Como os dados de urnas eletrônicas e doações do TSE são gigantescos, tudo precisa ser guardado em bancos de dados analíticos rápidos, garantindo que o aplicativo abra rápido no celular sem engasgar."
        ),
        (
            10,
            "Como técnicas de Inteligência Artificial e Processamento de Linguagem Natural podem ajudar?",
            "A inteligência artificial pode ajudar demais em uma coisa que afasta todo mundo da política: aquele \"juridiquês\" chato e enrolado que os deputados usam nas leis. A gente pode usar modelos de linguagem para ler projetos de dezenas de páginas e gerar resumos curtos, em bom português e fáceis de entender, explicando exatamente o que aquela proposta vai mudar na vida prática do cidadão comum. Além disso, as técnicas de processamento de linguagem natural servem para analisar os discursos e postagens dos políticos ao longo dos anos, mapeando como o posicionamento deles foi mudando e ajudando a identificar mentiras ou contradições de forma rápida durante debates eleitorais."
        ),
        (
            11,
            "Como o aprendizado de máquina pode auditar gastos públicos e apoiar o eleitor?",
            "Dá para usar o aprendizado de máquina para vigiar as contas públicas de um jeito muito eficiente. Uma ideia excelente é fazer o que a Operação Serenata de Amor fez com a robô Rosie: treinar algoritmos de detecção de anomalias para varrer as notas fiscais da cota parlamentar e acusar gastos absurdos, como refeições com valores fora da realidade, notas fiscais suspeitas em empresas de fachada ou gastos bizarros com combustível. Já do lado do eleitor, a gente pode usar cálculos de similaridade matemática para comparar as respostas do cidadão com as votações do plenário, entregando um cálculo de afinidade muito mais honesto e preciso do que qualquer pesquisa de opinião tradicional."
        ),
        (
            12,
            "Quais cuidados éticos, de imparcialidade e sustentabilidade o projeto deve ter?",
            "Esse ponto é fundamental, porque se a plataforma parecer que tem lado ou partido, ela perde a credibilidade na hora. Para evitar isso, o projeto tem que ser totalmente de código aberto (open source), para qualquer um poder auditar como as contas e as checagens são feitas. Tudo o que for mostrado tem que estar amparado estritamente em documentos oficiais públicos, sem opiniões pessoais ou ataques desnecessários. Além disso, temos que respeitar a privacidade e a LGPD, garantindo que as escolhas e o voto do usuário fiquem anônimos no celular dele. E para não ser comprada por ninguém, a plataforma deve se manter com editais acadêmicos, apoio de organizações civis e financiamento coletivo dos próprios cidadãos."
        ),
        (
            13,
            "Como transformar essa proposta em um projeto prático de graduação ou portfólio (PoC/TCC)?",
            "Para tirar essa ideia do papel e não ficar só na teoria, o segredo é começar pequeno com um protótipo focado. A gente poderia limitar o escopo inicial aos 53 deputados federais de Minas Gerais na atual legislatura, integrando os dados da API da Câmara com as contas do TSE e criando uma versão inicial funcional da Bússola Cívica e do monitor de gastos da cota parlamentar. Isso é plenamente viável de fazer durante o curso, resolve um problema real da sociedade e tem tudo para virar um Trabalho de Conclusão de Curso (TCC) de muito destaque no DCC/UFMG, além de ser aquele tipo de projeto prático que enche os olhos de qualquer recrutador numa entrevista técnica de emprego."
        )
    ]
    
    for num, q, a in perguntas_respostas:
        pdf.add_qa(num, q, a)
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'discussao_2_respostas.pdf')
    pdf.output(output_path)
    print(f"Sucesso: {output_path}")

if __name__ == '__main__':
    build_pdf()
