# Ouvidoria

### Arquivos do projeto:
- **MainMenuFinal.py**
    - Arquivo principal do projeto atualizado
- **mainFinal.py**
    - Versão desatualizada do arquivo principal
- **ouvidoria.py**
    - Versão desatualizada do arquivo com as funções do projeto
- **ouvidoriaFinal.py**
    - Versão finalizada das funções do projeto
- **operacoesbd.py**
    - Arquivos contendo as funções para operações com banco de dados (explicado melhor a seguir)

### Operações BD

- **Abrir banco de dados**

    *Tem como função estabelecer a conexão com o banco de dados*

    * Recebe como parâmetros: 
        - Host (Máquina do banco de dados)
        - User (Usuário que irá ter acesso ao banco de dados)
        - Password (Senha do banco de dados)
        - Database (Nome do banco de dados)
        
- **Encerrar banco de dados**

    *Tem como função encerrar a conexão com o banco de dados após a utilização*
    - Recebe como parâmetros:
        - Connection (Variável de conexão com o banco de dados)   
    
- **Insert no banco de dados**

    *Tem como função inserir ocorrências no banco de dados da ouvidoria*
    - Recebe como parâmetros:
        - Connection (Variável de conexão com o banco de dados)
        - SQL (Consulta em linguagem sql)
        - Dados (Dados que serão inseridos no banco de dados)
        
- **Listar banco de dados**

    *Tem como função receber o select do banco de dados para exibir para o usuário*
    - Recebe como parâmetros
        - Connection (Variável de conexão com o banco de dados)
        -  SQL (Consulta em linguagem sql)

- **Atualizar banco de dados**

  *Tem como função alterar informações já existentes no banco de dados*
    - Recebe como parâmetros:
        - Connection (Variável de conexão com o banco de dados)
        - SQL (Consulta em linguagem sql)
        - Dados (Novos dados que serão inseridos no banco de dados)
        
- **Excluir banco de dados**

  *Tem como função excluir alguma linha da tabela onde estão armazenados as ocorrências*
    - Recebe como parâmetros:
        - Connection (Variável de conexão com o banco de dados)
        - SQL (Consulta em linguagem sql)
        - Dados (Dado da linha que será excluída da tabela(Geralmente o id(primary key)))
    

  
    
    
        

       


        