

consulta_usuario_senha = '''SELECT count(1), ID 
                              FROM Users 
                             WHERE username = ? 
                               AND password = ?'''


consulta_email = '''SELECT count(1) 
                      FROM Users 
                      WHERE Email = ?'''

recupera_senha = '''SELECT Password 
                      FROM Users 
                     WHERE Email = ? '''

consulta_usuario = '''SELECT count(1) 
                        FROM Users 
                       WHERE username = ?'''                     

insere_usuario_banco = '''
                      INSERT INTO Users (name, username, email, cpf, password) 
                      VALUES (?, ?, ?, ?, ?)'''

listar_receitas = '''SELECT ID, NAME 
                       FROM Recipe 
                      WHERE UserID = ?'''                      

adicionar_receita = '''INSERT INTO Recipe (Name, UserID) 
                       VALUES (?, ?)'''

deletar_receita = '''DELETE FROM Recipe WHERE ID = ?'''