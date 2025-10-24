"""
simulate_db.py

Lê o arquivo banco.sql, converte instruções que não existem no SQLite
e executa em um banco em memória (sqlite3). Imprime o SQL e o resultado
do SELECT * FROM produtos para servir como 'prints' da simulação.
"""
import sqlite3
import re
from pathlib import Path

SQL_FILE = Path(__file__).with_name('banco.sql')

def load_sql(path):
    text = path.read_text(encoding='utf-8')
    print('--- Conteúdo de banco.sql ---')
    print(text)
    return text

def adapt_sql_for_sqlite(sql_text):
    # Remove CREATE DATABASE and USE statements
    sql = re.sub(r"CREATE DATABASE[^;]+;", "", sql_text, flags=re.IGNORECASE)
    sql = re.sub(r"USE[^;]+;", "", sql, flags=re.IGNORECASE)

    # Convert AUTO_INCREMENT to AUTOINCREMENT and INT to INTEGER primary key for sqlite
    sql = re.sub(r"INT\s+AUTO_INCREMENT\s+PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT", sql, flags=re.IGNORECASE)

    # SQLite uses REAL or NUMERIC for decimals; keep as REAL
    sql = re.sub(r"DECIMAL\(\d+,\s*\d+\)", "REAL", sql, flags=re.IGNORECASE)

    # Remove MySQL style backticks if any
    sql = sql.replace('`', '')

    # Split into statements
    stmts = [s.strip() for s in sql.split(';') if s.strip()]
    return stmts

def execute_statements(statements):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    for stmt in statements:
        try:
            cur.execute(stmt)
        except Exception as e:
            print(f"-- aviso ao executar: {stmt[:60]}... -> {e}")
    conn.commit()
    return conn, cur

def show_products(cur):
    print('\n--- Resultado: SELECT * FROM produtos ---')
    try:
        cur.execute('SELECT * FROM produtos')
        rows = cur.fetchall()
        if not rows:
            print('(nenhuma linha encontrada)')
            return
        # print header
        cols = [d[0] for d in cur.description]

        # calcular largura de cada coluna
        col_widths = []
        for i, c in enumerate(cols):
            maxw = len(c)
            for r in rows:
                v = '' if r[i] is None else str(r[i])
                if len(v) > maxw:
                    maxw = len(v)
            col_widths.append(maxw)

        # montar formato
        fmt = ' | '.join('{:' + str(w) + '}' for w in col_widths)
        sep = '-+-'.join('-' * w for w in col_widths)

        print(fmt.format(*cols))
        print(sep)
        for r in rows:
            print(fmt.format(*[('' if x is None else str(x)) for x in r]))
    except Exception as e:
        print('Erro ao consultar produtos:', e)

def main():
    if not SQL_FILE.exists():
        print('Arquivo banco.sql não encontrado em', SQL_FILE)
        return
    sql_text = load_sql(SQL_FILE)
    stmts = adapt_sql_for_sqlite(sql_text)
    conn, cur = execute_statements(stmts)
    show_products(cur)
    conn.close()

if __name__ == '__main__':
    main()
