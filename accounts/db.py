import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def createDB(connection):
    users_query = """
    CREATE TABLE IF NOT EXISTS user(
        empresa VARCHAR,
        patente VARCHAR,
        chofer VARCHAR,
        max_litros INTEGER,
        tagcamion VARCHAR,
        tagchofer VARCHAR,
        PRIMARY KEY(tagcamion, tagchofer)
    )    
    """
    log_query = """
    CREATE TABLE IF NOT EXISTS log(
        id INTEGER PRIMARY KEY,
        empresa VARCHAR,
        patente VARCHAR,
        chofer VARCHAR,
        fecha TIMESTAMP,
        litros INTEGER NULL,
        remito INTEGER
    )
    """
    cursor = connection.cursor()
    cursor.execute(users_query)
    cursor.execute(log_query)
    connection.commit()


def test():
    connection = sqlite3.connect('test.db')
    createDB(connection)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user VALUES('El Lucero de Tandil','AAA 000','Nicolás Dazeo', 275, '010213e000140301622780038d', '00008633')")
    cursor.execute("INSERT INTO user VALUES('El Lucero de Tandil','AAA 000','Nicolás Laugas', 275, '00008633', '00008633')")
    connection.commit()
    for row in cursor.execute("SELECT * FROM user"):
        print(row)
    return connection

if __name__ == "__main__":
    test()