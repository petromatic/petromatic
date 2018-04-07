from .user import User
from datetime import datetime

class LocalUser(object):
    def __init__(self, row, connection):
        super().__init__()
        self._credit = row['max_litros']
        self._connection = connection
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO 
                log(empresa,patente,chofer,fecha)
            VALUES (?,?,?,?)
        """, row['empresa'], row['patente'],row['chofer'],datetime.now())
        self._connection.commit()

    def addCharge(self, charge, fmTransaction):
        self._credit -= charge
        cursor = self._connection.cursor()
        cursor.execute("""
            UPDATE 
                log
            SET
                litros = ?, remito = ?
            WHERE 
                litros = NULL AND remito = NULL
        """, charge, fmTransaction)
        self._connection.commit()

    def getVehicleDict(self):
        return {}

    def getDriverDict(self):
        return {}
