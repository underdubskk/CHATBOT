import os
import time

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Guido Van Rossum, um programador de computador na Holanda, criou o Python. Ele começou em 1989 no Centrum Wiskunde & Informatica (CWI), inicialmente como um projeto de hobby para se manter ocupado durante o Natal.{os.linesep}')
    
    elif resposta == '2':
        print(f'{os.linesep}{nome} O Python é uma linguagem de programação amplamente usada em aplicações da Web, desenvolvimento de software, ciência de dados e machine learning (ML). Os desenvolvedores usam o Python porque é eficiente e fácil de aprender e pode ser executada em muitas plataformas diferentes.{os.linesep}')  
    
    elif resposta == '3':
        print(f'{os.linesep}{nome} A resposta é sim. Uma das principais razões para aprender Python é a sua versatilidade e ampla aplicabilidade. Python pode ser usado em uma variedade de áreas, desde desenvolvimento web e científico até automação de tarefas e inteligência artificial.{os.linesep}')  
    
    elif resposta == '4':
        print(f'{os.linesep}{nome} Lançado em 1991, o Python foi criado pelo matemático e programador holandês Guido van Rossum, que, na época, trabalhava no Centrum Wiskunde & Informatica (CWI), em Amsterdã. Curiosamente, o Python recebeu esse nome em homenagem ao seriado de humor britânico Monty Python\'s Flying Circus.{os.linesep}')  
    
    elif resposta == '5':
        print(f'{os.linesep}{nome} Python é uma linguagem amigável para iniciantes com sintaxe semelhante à do inglês. SQL é uma linguagem diferente com propósitos distintos e algumas variações que podem ser complexas.{os.linesep}')  
    
    elif resposta == '6':
        print(f'{os.linesep}{nome} Para usar o Python de forma eficiente, você precisa dominar algumas habilidades técnicas importantes: Conhecimento da linguagem de programação Python; Manipulação e análise de dados; Visualização de dados; Resolução de problemas; Domínio de técnicas de codificação.{os.linesep}')  
    
    elif resposta == '7':
        print(f'{os.linesep}{nome} O Python não roda apenas no Linux. Ele é uma linguagem de programação multiplataforma, o que significa que pode ser executado em diversos sistemas operacionais, incluindo Windows, macOS e Linux.{os.linesep}')  
    
    elif resposta == '8':
        print(f'{os.linesep}{nome} Sim, é possível desenvolver aplicações web em Python! A linguagem Python é muito popular para desenvolvimento web, e existem diversos frameworks e bibliotecas que facilitam o processo.{os.linesep}')  
    
    elif resposta == '9':
        print(f'{os.linesep}{nome} A estabilidade do Python é um ponto forte da linguagem. Ela existe desde 1991 e é considerada uma das linguagens de programação mais populares e estáveis. O Python é constantemente atualizado e mantido por uma grande comunidade de desenvolvedores.{os.linesep}')  
    
    elif resposta == '10':
        print(f'{os.linesep}{nome} É difícil dizer exatamente quantas pessoas usam Python, mas há milhões de usuários, já que o Python está disponível para download gratuito e é amplamente utilizado em várias áreas.{os.linesep}')  
    
    elif resposta == '11':
        print(f'{os.linesep}{nome} A resposta para essa pergunta é um pouco complexa. Alguns artigos defendem que o Python pode não ser a melhor escolha para iniciantes, pois a simplicidade pode mascarar conceitos importantes. Outros artigos destacam que o Python é fácil de aprender e possui uma grande comunidade que oferece suporte e recursos para iniciantes.{os.linesep}')  
    
    elif resposta == '12':
        print(f'{os.linesep}{nome} O Python é uma linguagem de programação livre e de código aberto. Isso significa que você pode usar, copiar, modificar e distribuir o Python livremente, desde que mantenha os direitos autorais e a licença original.{os.linesep}')                                
    
    elif resposta == '13':
        print(f'{os.linesep}{nome} No Python 3.12 é a versão estável mais recente da linguagem de programação Python, com uma combinação de alterações na linguagem e na biblioteca padrão. As alterações da biblioteca se concentram na limpeza de APIs descontinuadas, usabilidade e correção. É importante notar que o pacote distutils foi removido da biblioteca padrão. O suporte ao sistema de arquivos em os e pathlib teve uma série de melhorias e vários módulos têm melhor desempenho.{os.linesep}')  
    
    elif resposta == '14':
        print(f'{os.linesep}{nome} Alguns projetos populares em Python incluem: Desenvolvimento Web, Machine Learning, Ciência de Dados, e Jogos.{os.linesep}')        
    
    elif resposta == '15':
        print(f'{os.linesep}{nome} Sim, existem muitos livros sobre Python! Você pode encontrá-los em sites como a Amazon.{os.linesep}')  

    else:
        print('                       Digite apenas um número de 1 a 15')

def start():
    # apresentação do chatbot
    print('-' * 88)
    print('        | Olá! Bem-vindo ao nosso CHATBOT - Nosso assunto de hoje será o PYTHON!')
    print('-' * 88)

    time.sleep(0.5)
    # agrupamento de informações do nome do usuário
    nome = input('                       > Digite o seu nome: ')

    time.sleep(0.5)
    # agrupamento de informações do e-mail do usuário
    email = input('                       > Digite o seu e-mail: ')

    while True:
        time.sleep(1.5)
        # oferecer o menu de opções
        print('-' * 88)
        resposta = input(f'                           O que gostaria de saber hoje?{os.linesep}[1] - Quem foi o fundador do Python?{os.linesep}[2] - Qual é o propósito do Python?{os.linesep}[3] - Vale a pena estudar Python?{os.linesep}[4] - Por que o nome Python?{os.linesep}[5] - Qual é a diferença entre Python e SQL?{os.linesep}[6] - Quais são as habilidades técnicas necessárias para usar o Python de forma eficiente?{os.linesep}[7] - O Python só roda no Linux?{os.linesep}[8] - Dá para desenvolver Web em Python?{os.linesep}[9] - Quão estável é o Python?{os.linesep}[10] - Quantas pessoas usam o Python?{os.linesep}[11] - Python é uma boa linguagem para iniciantes?{os.linesep}[12] - Existem restrições de direitos autorais sobre o uso de Python?{os.linesep}[13] - O que há de novo no Python 3.12?{os.linesep}[14] - Existe algum projeto significativo feito em Python?{os.linesep}[15] - Existem livros sobre o Python?{os.linesep}[0] - Sair{os.linesep}')

        # oferecer o processo de respostas
        if resposta == '0':
            print('                     Obrigado por usar o CHATBOT. Até mais!')
            break

        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()