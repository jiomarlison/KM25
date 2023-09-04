import sqlite3
from contextlib import closing
import datetime as dttm

with closing(sqlite3.connect("Petrolina_Projetos.db")) as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS HORARIOS_KM_25"
            " (ID INTEGER PRIMARY KEY AUTOINCREMENT,"
            " DIA TEXT NOT NULL,"
            " VEICULO TEXT,"
            " HORARIO TEXT NOT NULL,"
            " AREA TEXT NOT NULL"
            ")"
        )
        try:
            cursor.execute(
                "INSERT INTO HORARIOS_KM_25(DIA, VEICULO, HORARIO, AREA)"
                "VALUES"
                f"('SEGUNDA À SEXTA', '2ª', '{dttm.datetime.today()}', 'VILA')"
            )
        except:
            print("Já tem")
        registros = cursor.execute("SELECT * FROM HORARIOS_KM_25").fetchall()
        print("Registros Banco de Dados")
        for registro in registros:
            print(registro)
        tabelas_banco = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
        print("Tabelas do Banco:")
        for tabela in tabelas_banco:
            print(tabela[1])
            informacoes_tabela = cursor.execute(f'pragma table_info("{tabela[1]}")').fetchall()
            print("Informações Tabelas")
            for informacao_tabela in informacoes_tabela:
                print(informacao_tabela[1:3])


        conexao.commit()