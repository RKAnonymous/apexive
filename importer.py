import json
from datetime import datetime
from tqdm import tqdm
from utils import QuickConnection, DB_CONF, IMPORTER_FILE


class Importer:
	"""
	Data importer

	:param: source  	 Source JSON file path
	:param: destination  Destination JSON file path
	:param: db_conf      Database config parameters file path or dict object
	"""
	def __init__(self, source=None, destination=None, db_conf=None):
		self.source = source or IMPORTER_FILE
		self.destination = destination
		self.db_conf = db_conf

	def read(self):
		"""Read JSON file."""
		with open(self.source, encoding="utf-8") as file:
			data = file.read()
			reader = json.loads(data.replace('\\"', '"').replace('\\\\"', '\\"'))

		return reader

	def prettify(self):
		"""Prettify JSON data."""
		data = self.read()
		with open(self.destination, "w") as f:
			f.write(json.dumps(data, indent=2))

	def get_tables(self):
		"""
		Get `table` field values in order to identify the DB structure.
		NOTE: For one time manual usage.
		"""
		data = self.read()
		tables = []
		for datum in data:
			table = datum["table"].lower()
			if table not in tables:
				tables.append(table)

		return tables

	def filter_by(self, key, value):
		"""Filter JSON by key:value pairs."""
		func = lambda x: True if x[key].lower() == value else False
		return list(filter(func, self.read()))

	def push(self):
		"""
		Save data to Database.
		:return:
		"""
		tables = self.get_tables()
		for table in tables:

			data = self.filter_by("table", table)
			for datum in data:
				datum["modified"] = datum.pop("_modified")
				datum["created_at"] = datetime.now().strftime("%Y-%m-%d")
				obj = datum.pop("meta")

				main_insert_query = self.insert_query("pilotlogheader", list(datum.keys()), list(datum.values()))
				table_insert_query = self.insert_query(table, list(obj.keys()), list(obj.values()))
				with QuickConnection(self.get_db_conf()) as db:
					conn, cursor = db
					cursor.execute(main_insert_query)
					cursor.execute(table_insert_query)
					conn.commit()
					# self.loader(len(list(data)))

		return True

	def insert_query(self, table: str, columns: list, values: list) -> str:
		"""
		Make DB insert queries dynamically.
		:param table: table_name
		:param columns: columns array
		:param values: values array
		:return:
		"""
		columns = ", ".join([f'"{col}"' if col == "table" or any(ch.isupper() for ch in col) else col for col in columns])
		values = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in values])
		return f"INSERT INTO pilotlog_{table.lower()} ({columns}) VALUES ({values}) RETURNING id;"

	def get_db_conf(self):
		if isinstance(self.db_conf, dict):
			return self.db_conf
		else:
			with open(self.db_conf, 'r') as f:
				return json.loads(f.read())

	def loader(self, length):
		for i in tqdm(range(round(length * 0.15))):
			pass


def main():
	parser = argparse.ArgumentParser(
		prog='Importer',
		description='Pull JSON data.'
	)

	parser.add_argument("-s", "--source", help="Source file with JSON formatted data.", default=IMPORTER_FILE, )
	parser.add_argument("-o", "--output", help="Destination file to save data in more python friendly structure.")
	parser.add_argument("-d", "--db-conf", help="Database config file(JSON) to push data to DB.")
	parser.add_argument("--save", help="Flag to save data to default db.")

	args = parser.parse_args()

	try:
		importer = Importer(source=args.source)

		if args.output:
			importer.destination = args.output
			importer.prettify()
			print(f"Saved to {importer.destination} file.")
		elif args.db_conf:
			importer.db_conf = args.db_conf
			importer.push()
			print("Pushed to provided DB.")
		elif args.save:
			importer.db_conf = DB_CONF
			importer.push()
			print("Pushed to default DB.")

	except BaseException as exc:
		print(f"{exc.__class__.__name__}: {exc.args}")
	finally:
		print("Importer stopped.")


if __name__ == "__main__":
	import argparse

	main()
