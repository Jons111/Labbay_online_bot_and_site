import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE myfiles_menu (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO myfiles_menu(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO myfiles_menu(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_menu
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_menu where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_menu WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def filter_product(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_menu where id=1 AND Name='John'"
        sql = "SELECT * FROM  myfiles_product WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_menu;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE myfiles_menu SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE myfiles_menu SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM myfiles_menu WHERE TRUE", commit=True)

    def anketa(self, id: int, ism: str, fam: str ,yosh:int, tel:str, jins:str, shaxar:str, username:str):
        # SQL_EXAMPLE = "INSERT INTO myfiles_Anketa(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO  myfiles_Anketa (id, ism, fam, yosh, tel, jins ,shaxar, username) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """

        self.execute(sql, parameters=(id, ism,fam,yosh,tel,jins,shaxar,username), commit=True)

    def select_product(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_menu where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_Product WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def add_sold_product(self, id: int, nomi: str, narxi: int, miqdori:int, tur:str, username : str ):
        # SQL_EXAMPLE = "INSERT INTO myfiles_Anketa(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
          INSERT INTO  myfiles_Sotib_olingan_maxsulotlar (id, nomi, narxi, miqdori, tur, username) VALUES(?, ?, ?, ?, ?, ?)
          """

        self.execute(sql, parameters=(id, nomi, narxi, miqdori, tur, username), commit=True)

    def select_sold_product(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_menu where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_Sotib_olingan_maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_sold_product(self):
        sql = """
           SELECT * FROM myfiles_Sotib_olingan_maxsulotlar
           """
        return self.execute(sql, fetchall=True)

    def update_sold_product(self, miqdori,narxi, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
           UPDATE myfiles_Sotib_olingan_maxsulotlar  SET miqdori=?, narxi=?  WHERE id=?
           """
        return self.execute(sql, parameters=(miqdori,narxi, id), commit=True)

    def select_all_products(self):
        sql = """
           SELECT * FROM myfiles_Product
           """
        return self.execute(sql, fetchall=True)
    def select_all_type(self):
        sql = """
           SELECT * FROM myfiles_Type
           """
        return self.execute(sql, fetchall=True)

    def select_type(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_menu where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_Type WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)
    def delete_sold_product(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_menu where id=1 AND Name='John'"
        sql = "DELETE  FROM myfiles_Sotib_olingan_maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
