import psycopg2 as db


class Postgresdb:

	def __init__(self):
		self.database = None
		self.cursor = None
		

	def connect(self):
		from settings import HOST, USER, PASSWORD, DATABASE_NAME
		self.database = db.connect(host=HOST, user=USER, password=PASSWORD, dbname=DATABASE_NAME) 
		self.cursor = self.database.cursor()

	def create_table(self, name):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS {0} (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, content TEXT NOT NULL);".format(name))
		self.database.commit()

	def close(self):
		self.database.close()


	def inserti(self, title, content):
		from settings import TABLE_NAME
		self.cursor.execute("INSERT INTO {NAME} (title, content) VALUES ('{0}', '{1}')".format(title, content, NAME = TABLE_NAME))
		self.database.commit()


