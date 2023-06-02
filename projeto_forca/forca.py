"""PROJETO DA FORCA"""

import random

# função para escolher a palavra de acordo com o tema da lista de palavras para o jogo de forca
def escolher_palavra(tema):
    if tema == 1:
        palavras = ['python', 'java', 'ruby', 'csharp']
    elif tema == 2:
        palavras = ["ihc", "programacao", "frontend"]
    elif tema == 3:
        palavras =["fernanda","emanuel","lidiane", "camila"]
    else:
        return None
    palavra_sorteada = random.choice(palavras)
    return palavra_sorteada

# Função para desenhar a forca conforme for errando a letra da palavra
def desenhar_forca(tentativas):
    desenhos_forca = [
        """
        +---+
        | |
        |
        |
        |
        |
        =========""",
        """
        +---+
        |   |
        |   O 
        |
        |
        |
        =========""",
        """
        +---+
        |   |
        |   O 
        |   |
        |
        |
        =========""",
        """
        +---+
        |   |
        |   O 
        |  /| 
        |
        |
        =========""",
        """
        +---+
        |   |
        |   O 
        |  /|\ 
        |
        |
        =========""",
        """
        +---+
        |   |
        |   O 
        |  /|\ 
        |  / 
        |
        =========""",
        """
        +---+1
        |   |
        |   O 
        |  /|\ 
        |  / \ 
        |
        ========="""
        ]
    print(desenhos_forca[6 - tentativas])

# Função para iniciar o jogo escolhendo o tema
def sortear_palavra():
    print("""
            **   *******     ********    *******     *******       **       ********   *******   *******     ******      **    
            /**  **/////**   **//////**  **/////**   /**////**     ****     /**/////   **/////** /**////**   **////**    ****   
            /** **     //** **      //  **     //**  /**    /**   **//**    /**       **     //**/**   /**  **    //    **//**  
            /**/**      /**/**         /**      /**  /**    /**  **  //**   /******* /**      /**/*******  /**         **  //** 
            /**/**      /**/**    *****/**      /**  /**    /** **********  /**////  /**      /**/**///**  /**        **********
        **  /**//**     ** //**  ////**//**     **   /**    ** /**//////**  /**      //**     ** /**  //** //**    **/**//////**
        //*****  //*******   //********  //*******    /*******  /**     /**  /**       //*******  /**   //** //****** /**     /**
        /////    ///////     ////////    ///////     ///////   //      //   //         ///////   //     //   //////  //      // """)
    print("\nVocê terá 6 tentativas para acertar a palavra escolhida!!")
    print("\nTemas disponíveis:")
    temas ={
        1: "Programação",
        2: "Disciplinas",
        3: "Alunos"
    }
    for tema, descricao in temas.items():
        print(f"\n {tema}:{descricao}")

    tema_escolhido = None

    while tema_escolhido is None:
        try:
            tema = input("\nEscolha apenas um tema para começarmos a jogar: ")
            tema_sem_especiais = ''.join(c for c in tema if c.isdigit())
            if len(tema_sem_especiais) == 1:
                tema_escolhido = int(tema_sem_especiais)
            else:
                print("Escolha inválida. Por favor, insira apenas um número, de acordo com o tema escolhido: ")
        except ValueError:
            print("Escolha inválida. Por favor, insira apenas um número, de acordo com o tema escolhido: ")

    if tema_escolhido in temas:
        palavra_sorteada = escolher_palavra(tema_escolhido)
        
        palavra_oculta = "_" * len(palavra_sorteada)
        print('\nA palavra tem', len(palavra_sorteada), 'letras:', palavra_oculta)
        jogar_forca(palavra_sorteada, palavra_oculta)
    else:
        print("Tema inválido!")
        sortear_palavra()

# Função principal para jogar o jogo da forca
def jogar_forca(palavra_sorteada, palavra_oculta):
    tentativas = 6
    letras_erradas = []
    letras_certas = []
    while tentativas > 0:
        letra = input("\nDigite uma letra: ").lower()
        if not letra.isalpha():
            print("Você não digitou uma letra. Tentativa inválida!!")
            continue
        if letra in letras_certas or letra in letras_erradas or letra in palavra_oculta:
            print("Você já tentou essa letra!")
            continue
        if letra in letras_erradas or letra in palavra_oculta:
            print("Esta letra já foi tentada!!")
            if letra in palavra_oculta:
                continue
        if len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue
        if letra in palavra_sorteada:
            palavra_oculta = atualizar_palavra_oculta(palavra_sorteada, palavra_oculta, letra)
            print(palavra_oculta)
        if palavra_oculta == palavra_sorteada:
            print("""
                    *******      **     *******       **     ******   ******** ****     **  ********
                    /**////**    ****   /**////**     ****   /*////** /**///// /**/**   /** **////// 
                    /**   /**   **//**  /**   /**    **//**  /*   /** /**      /**//**  /**/**       
                    /*******   **  //** /*******    **  //** /******  /******* /** //** /**/*********
                    /**////   **********/**///**   **********/*//// **/**////  /**  //**/**////////**
                    /**      /**//////**/**  //** /**//////**/*    /**/**      /**   //****       /**
                    /**      /**     /**/**   //**/**     /**/******* /********/**    //*** ******** 
                    //       //      // //     // //      // ///////  //////// //      /// ////////  """)
            break
        if letra not in palavra_sorteada:
            letras_erradas.append(letra)
            letras_erradas = list(set(letras_erradas)) # Remover letras duplicadas
            tentativas -= 1
            desenhar_forca(tentativas)
            print("\nLetras erradas:", letras_erradas)
            print("\nTentativas restantes:", tentativas)
        if tentativas == 0:
            desenhar_forca(tentativas)
            print(f"\nVocê foi enforcado! A palavra correta era: {palavra_sorteada}!!")

    jogar_novamente()

# Função para atualizar a palavra oculta com as letras corretamente adivinhadas
def atualizar_palavra_oculta(palavra_sorteada, palavra_oculta, letra):
    nova_palavra_oculta = ""
    for i in range(len(palavra_sorteada)):
        if palavra_sorteada[i] == letra:
            nova_palavra_oculta += letra
        else:
            nova_palavra_oculta += palavra_oculta[i]
    return nova_palavra_oculta

# Função para jogar novamente ou sair do jogo
def jogar_novamente():
    opcao = input("\nGostaria de jogar novamente?")
    if opcao.lower() == "sim" or opcao == "s":
        sortear_palavra()
    else:
        print("\nObrigado por jogar!")

sortear_palavra()
