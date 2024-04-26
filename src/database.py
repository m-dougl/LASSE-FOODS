import sqlite3
import pandas as pd


class LasseFoodsDB:
    def __init__(self, db_path) -> None:
        self.connection = sqlite3.connect(db_path)

    def create_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS pedidos(
                id INTEGER PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                pedido TEXT NOT NULL
            )
        """

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def add_data(self, username: str, food_order: str) -> None:
        query = """
            INSERT INTO pedidos(
                nome,
                pedido
            )
            VALUES(
                ?, ?
            )
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (username, food_order))
        self.connection.commit()

    def get_data(self):
        query = """
            SELECT * FROM pedidos
        """

        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=["id", "nome", "pedido"])
        return df