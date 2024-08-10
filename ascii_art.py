def get_hangman_ascii_art():
    return [
    # Game Over (0 lives)
    '''
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |    
    ------
    ''',
    # 1 life left
    '''
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |    
    ------
    ''',
    # 2 lives left
    '''
      ------
      |    |
      |    O
      |   /|\\
      |    
      |    
    ------
    ''',
    # 3 lives left
    '''
      ------
      |    |
      |    O
      |   /|
      |    
      |    
    ------
    ''',
    # 4 lives left
    '''
      ------
      |    |
      |    O
      |    |
      |    
      |    
    ------
    ''',
    # 5 lives left
    '''
      ------
      |    |
      |    O
      |   
      |    
      |    
    ------
    ''',
    # 6 lives left
    '''
      ------
      |    |
      |    
      |   
      |    
      |    
    ------
    '''
]



def cipher_ascii_art():
    print(''' 
     a88888b.  .d888888   88888888b .d88888b   88888888b  888888ba      a88888b. dP  888888ba  dP     dP   88888888b  888888ba  
    d8'   `88 d8'    88   88        88.    "'  88         88    `8b    d8'   `88 88  88    `8b 88     88   88         88    `8b 
    88        88aaaaa88a a88aaaa    `Y88888b. a88aaaa    a88aaaa8P'    88        88 a88aaaa8P' 88aaaaa88a a88aaaa    a88aaaa8P' 
    88        88     88   88              `8b  88         88   `8b.    88        88  88        88     88   88         88   `8b. 
    Y8.   .88 88     88   88        d8'   .8P  88         88     88    Y8.   .88 88  88        88     88   88         88     88 
     Y88888P' 88     88   88888888P  Y88888P   88888888P  dP     dP     Y88888P' dP  dP        dP     dP   88888888P  dP     dP 
    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    ''')


