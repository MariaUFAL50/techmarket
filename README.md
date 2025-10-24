# TechMarket

Projeto de exemplo para simular armazenamento de dados (sem servidor real).

Arquivos criados:

- `banco.sql` - contém as instruções SQL solicitadas (CREATE DATABASE, USE, CREATE TABLE, INSERTs).
- `simulate_db.py` - script Python que adapta e executa o SQL em um banco SQLite em memória e mostra o resultado de `SELECT * FROM produtos`.

Como rodar (Windows PowerShell):

```powershell
# garantir que Python 3 esteja instalado
python --version

# executar o script
python simulate_db.py
```

O script imprimirá o SQL lido e o resultado do SELECT, que servem como os "prints obrigatórios".

Notas:

- A simulação usa SQLite em memória. O script remove/ignora `CREATE DATABASE` e `USE` e converte `AUTO_INCREMENT` e `DECIMAL` para tipos compatíveis com SQLite.
- Se quiser executar o SQL original em MySQL real, use MySQL Workbench ou DBeaver importando `banco.sql`.
