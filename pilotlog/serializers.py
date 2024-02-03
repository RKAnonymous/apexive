from rest_framework import serializers
from pilotlog import models as pl_models
from datetime import datetime


class AirfieldSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.Airfield
		fields = "__all__"


class AircraftSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.Aircraft
		fields = "__all__"


class PilotSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.Pilot
		fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.Flight
		fields = "__all__"


class QualificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.Qualification
		fields = "__all__"


class LimitRulesSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.LimitRules
		fields = "__all__"


class MyQuerySerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.MyQuery
		fields = "__all__"


class MyQueryBuildSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.MyQueryBuild
		fields = "__all__"


class ImagePicSerializer(serializers.ModelSerializer):
	class Meta:
		model = pl_models.Imagepic
		fields = "__all__"


class PilotlogHeaderSerializer(serializers.ModelSerializer):

	class Meta:
		model = pl_models.PilotlogHeader
		fields = "__all__"


class SettingConfigSerializer(serializers.ModelSerializer):

	class Meta:
		model = pl_models.SettingConfig
		fields = "__all__"


class AircraftForExportSerializer(serializers.ModelSerializer):
	AircraftID = serializers.CharField(source='AircraftCode')
	EngineType = serializers.CharField(source='EngType')
	HighPerformance = serializers.BooleanField(source='HighPerf')

	# EquipmentType = serializers.CharField()
	# TypeCode = serializers.CharField()
	# Year = serializers.IntegerField()
	# GearType = serializers.CharField()
	# Pressurized = serializers.BooleanField()
	# TAA = serializers.BooleanField()

	class Meta:
		model = pl_models.Aircraft
		fields = (
			'AircraftID',
			'Make',
			'Model',
			'Category',
			'Class',
			'EngineType',
			'Complex',
			'HighPerformance',

			# 'EquipmentType',
			# 'TypeCode',
			# 'Year',
			# 'GearType',
			# 'Pressurized',
			# 'TAA'
		)


class FlightExportSerializer(serializers.ModelSerializer):
	Date = serializers.DateField(source='DateBASE')
	AircraftID = serializers.CharField(source='AircraftCode')
	HobbsStart = serializers.IntegerField(source='HobbsIn')
	HobbsEnd = serializers.IntegerField(source='HobbsOut')
	# From
	# To
	# Route
	# TimeOut
	# TimeOff
	# TimeOn
	# TimeIn
	# OnDuty
	# OffDuty
	# TotalTime
	# PIC
	# SIC
	# Night
	# Solo
	# CrossCountry
	# NVG
	# NVGOps
	# Distance
	# DayTakeoffs
	# DayLandingsFullStop
	# NightTakeoffs
	# NightLandingsFullStop
	# AllLandings
	# ActualInstrument
	# SimulatedInstrument
	# TachStart
	# TachEnd
	# Holds
	# Approach1
	# Approach2
	# Approach3
	# Approach4
	# Approach5
	# Approach6
	# DualGiven
	# DualReceived
	# SimulatedFlight
	# GroundTraining
	# InstructorName
	# InstructorComments
	# Person1
	# Person2
	# Person3
	# Person4
	# Person5
	# Person6
	# FlightReview
	# Checkride
	# IPC
	# NVGProficiency
	# FAA6158
	# [Text]CustomFieldName
	# [Numeric]CustomFieldName
	# [Hours]CustomFieldName
	# [Counter]CustomFieldName
	# [Date]CustomFieldName
	# [DateTime]CustomFieldName
	# [Toggle]CustomFieldName
	# PilotComments

	class Meta:
		model = pl_models.Flight
		fields = (
			'Date',
			'AircraftID',
			'HobbsStart',
			'HobbsEnd',
			# From
			# To
			# Route
			# TimeOut
			# TimeOff
			# TimeOn
			# TimeIn
			# OnDuty
			# OffDuty
			# TotalTime
			# PIC
			# SIC
			# Night
			# Solo
			# CrossCountry
			# NVG
			# NVGOps
			# Distance
			# DayTakeoffs
			# DayLandingsFullStop
			# NightTakeoffs
			# NightLandingsFullStop
			# AllLandings
			# ActualInstrument
			# SimulatedInstrument
			# TachStart
			# TachEnd
			# Holds
			# Approach1
			# Approach2
			# Approach3
			# Approach4
			# Approach5
			# Approach6
			# DualGiven
			# DualReceived
			# SimulatedFlight
			# GroundTraining
			# InstructorName
			# InstructorComments
			# Person1
			# Person2
			# Person3
			# Person4
			# Person5
			# Person6
			# FlightReview
			# Checkride
			# IPC
			# NVGProficiency
			# FAA6158
			# [Text]CustomFieldName
			# [Numeric]CustomFieldName
			# [Hours]CustomFieldName
			# [Counter]CustomFieldName
			# [Date]CustomFieldName
			# [DateTime]CustomFieldName
			# [Toggle]CustomFieldName
			# PilotComments
		)