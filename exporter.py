import csv
import json
from typing import Dict, Any
from datetime import datetime
from tqdm import tqdm
from utils import QuickConnection, DB_CONF, EXPORTER_FILE


class Exporter:
	"""
	Data exporter
	:param: template_file   Data structure template
	"""

	def __init__(self, template_file):
		self.template_file = template_file

	def get_template(self):
		"""
		Read corresponding CSV file and build exporter
		structure up to the fields provided in the file.
		:return: list
		"""
		template = {}
		with open(self.template_file, "r") as f:
			data = list(csv.reader(f))

			for idx, row in enumerate(data):
				col = row[0].lower()

				if "table" in col:
					table_name = col.split(" ")[0]
					template[table_name] = {f: t for f, t in zip(data[idx + 2], data[idx + 1])}
					print("\n".join(data[idx + 2]))

		return template

	def get_data(self):
		"""
		Pull data from DB.
		:return: list
		"""
		data = {}
		with QuickConnection(DB_CONF) as db:
			conn, cursor = db
			template = self.get_template()
			iter_by = list(template.keys())

			for table_name in iter_by:
				select_q = self.select_query(table_name, template[table_name].keys())
				cursor.execute(select_q)
				self.loader()
				data[table_name] = cursor.fetchall()

		return data

	def reformat(self) -> Dict[str, Any]:
		"""
		Reformat fields types up to the template given.
		:param: data => self.data
		:return: data
		"""

		data = self.get_data()
		# Do something

		return data

	def output(self, file=None, fmt="json"):
		"""
		Save reformatted data into pointed file..
		:return:
		"""
		file = file if file else str(datetime.now().strftime("%Y-%m-%d_%H:%M"))+".json"
		structured_data = self.reformat()
		with open(file, "w") as f:
			if fmt == "csv":
				writer = csv.writer(f)
				writer.writerows(structured_data)
			else:
				json.dump(structured_data, f)

	def select_query(self, table, columns) -> str:
		"""SQL SELECT query maker"""
		return f"SELECT {columns} FROM pilotlog_{table} ORDER BY id ASC;"

	def loader(self, length: int = 1000) -> None:
		"""
		Loader
		:rtype: None
		:param length: 
		"""
		for i in tqdm(range(round(length * 0.15))):
			pass


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(
		prog='Exporter',
		description='Pull data from Database in the structured format.'
	)

	parser.add_argument("-o", "--output", help="Destination file to save file.", default="output")
	parser.add_argument("-f", "--format", help="Destination file format to save file.", default="json")
	parser.add_argument("-t", "--template", help="Data structure template file.", default=EXPORTER_FILE)

# Asked format in exporter template
flight = {
	'Date': 'Date',
	'AircraftID': 'Text',
	'From': 'Text',
	'To': 'Text',
	'Route': 'Text',
	'TimeOut': 'hhmm',
	'TimeOff': 'hhmm',
	'TimeOn': 'hhmm',
	'TimeIn': 'hhmm',
	'OnDuty': 'hhmm',
	'OffDuty': 'hhmm',
	'TotalTime': 'Decimal',
	'PIC': 'Decimal',
	'SIC': 'Decimal',
	'Night': 'Decimal',
	'Solo': 'Decimal',
	'CrossCountry': 'Decimal',
	'NVG': 'Decimal',
	'NVGOps': 'Number',
	'Distance': 'Decimal',
	'DayTakeoffs': 'Number',
	'DayLandingsFullStop': 'Number',
	'NightTakeoffs': 'Number',
	'NightLandingsFullStop': 'Number',
	'AllLandings': 'Number',
	'ActualInstrument': 'Decimal',
	'SimulatedInstrument': 'Decimal',
	'HobbsStart': 'Decimal',
	'HobbsEnd': 'Decimal',
	'TachStart': 'Decimal',
	'TachEnd': 'Decimal',
	'Holds': 'Number',
	'Approach1': 'Packed Detail',
	'Approach2': 'Packed Detail',
	'Approach3': 'Packed Detail',
	'Approach4': 'Packed Detail',
	'Approach5': 'Packed Detail',
	'Approach6': 'Packed Detail',
	'DualGiven': 'Decimal',
	'DualReceived': 'Decimal',
	'SimulatedFlight': 'Decimal',
	'GroundTraining': 'Decimal',
	'InstructorName': 'Text',
	'InstructorComments': 'Text',
	'Person1': 'Packed Detail',
	'Person2': 'Packed Detail',
	'Person3': 'Packed Detail',
	'Person4': 'Packed Detail',
	'Person5': 'Packed Detail',
	'Person6': 'Packed Detail',
	'FlightReview': 'Boolean',
	'Checkride': 'Boolean',
	'IPC': 'Boolean',
	'NVGProficiency': 'Boolean',
	'FAA6158': 'Boolean',
	'PilotComments': 'Text'
}

# Format saved in Database using data from importer file
flight_model = {
	'Record_Modified': 'integer',
	'PF': 'boolean',
	'Pax': 'integer',
	'Fuel': 'integer',
	'Cargo': 'integer',
	'DeIce': 'boolean',
	'minEXAM': 'integer',
	'DateBASE': 'date',
	'FuelUsed': 'integer',
	'HobbsOut': 'integer',  # -> HobbsEnd
	'LdgNight': 'integer',  # Night
	'NextPage': 'boolean',
	'UserBool': 'boolean',
	'minINSTR': 'integer',
	'minNIGHT': 'integer',  # -> AllLandings
	'minPICUS': 'integer',
	'minTOTAL': 'integer',
	'ArrOffset': 'integer',
	'DateLOCAL': 'date',
	'DepOffset': 'integer',
	'ToTimeUTC': 'integer',
	'ArrTimeUTC': 'integer',
	'BaseOffset': 'integer',
	'DepTimeUTC': 'integer',
	'LdgTimeUTC': 'integer',
	'FuelPlanned': 'integer',
	'NextSummary': 'boolean',
	'ArrTimeSCHED': 'integer',
	'DepTimeSCHED': 'integer',
	'ToDay': 'integer',
	'minU1': 'integer',
	'minU2': 'integer',
	'minU3': 'integer',
	'minU4': 'integer',
	'minXC': 'integer',
	'LdgDay': 'integer',  # ->
	'LiftSW': 'integer',
	'ToEdit': 'boolean',
	'minAIR': 'integer',
	'minCOP': 'integer',
	'minIFR': 'integer',
	'minIMT': 'integer',
	'minPIC': 'integer',
	'minREL': 'integer',
	'minSFR': 'integer',
	'DateUTC': 'date',  # -> Date
	'HobbsIn': 'integer',  # -> HobbsStart
	'Holding': 'integer',
	'SignBox': 'integer',
	'ToNight': 'integer',
	'UserNum': 'integer',
	'minDUAL': 'integer',
	'Route': 'character varying',
	'AircraftCode': 'character varying',
	'ArrCode': 'character varying',
	'FlightNumber': 'character varying',
	'DepCode': 'character varying',
	'FlightSearch': 'character varying',
	'TagApproach': 'character varying',
	'ArrRwy': 'character varying',
	'DepRwy': 'character varying',
	'Pairing': 'character varying',
	'Remarks': 'character varying',
	'P1Code': 'character varying',
	'P2Code': 'character varying',
	'P3Code': 'character varying',
	'P4Code': 'character varying',
	'Report': 'character varying',
	'TagOps': 'character varying',
	'TagDelay': 'character varying',
	'Training': 'character varying',
	'FlightCode': 'character varying',
	'UserText': 'character varying',
	'TagLaunch': 'character varying',
	'CrewList': 'character varying',
	'TagLesson': 'character varying'
}
