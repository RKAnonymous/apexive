import os
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv


load_dotenv()

DB_CONF = dict(
	host=os.getenv("SQL_HOST"),
	database=os.getenv("SQL_DATABASE"),
	user=os.getenv("SQL_USER"),
	password=os.getenv("SQL_PASSWORD"),
	port=os.getenv("SQL_PORT")
)

IMPORTER_FILE = os.getenv("IMPORTER_FILE")
EXPORTER_FILE = os.getenv("EXPORTER_FILE")


class QuickConnection:
	def __init__(self, conf):
		self.ps_connection = psycopg2.connect(**conf)
		self.ps_cursor = self.ps_connection.cursor(cursor_factory=extras.DictCursor)

	def __enter__(self):
		return self.ps_connection, self.ps_cursor

	def __exit__(self, err_type, err_value, traceback):
		if err_type and err_value:
			self.ps_connection.rollback()
		self.ps_cursor.close()
		self.ps_connection.close()
		return False
