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


class AircraftDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = pl_models.Aircraft
		fields = (
			"id",
			"Model",
			"Company",
			"Class",
			"Power",
			"Rating",
			"Seats"
		)


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

	# def to_representation(self, instance):
	# 	represent = super(PilotlogHeaderSerializer, self).to_representation(instance)
	# 	represent.update(
	# 		{
	# 			"aircraft": AircraftSerializer().to_representation(instance.aircraft),
	# 			"airfield": AirfieldSerializer().to_representation(instance.airfield),
	# 			"flight": FlightSerializer().to_representation(instance.flight),
	# 			"pilot": PilotSerializer().to_representation(instance.pilot),
	# 			"qualification": QualificationSerializer().to_representation(instance.qualification),
	# 			"my_query": MyQuerySerializer().to_representation(instance.my_query),
	# 			"my_query_build": MyQueryBuildSerializer().to_representation(instance.my_query_build),
	# 			"image": ImagePicSerializer().to_representation(instance.image),
	# 			"setting_config": SettingConfigSerializer().to_representation(instance.setting_config),
	# 			"limit_rules": LimitRulesSerializer().to_representation(instance.limit_rules),
	# 		}
	# 	)
	# 	return represent


class SettingConfigSerializer(serializers.ModelSerializer):

	class Meta:
		model = pl_models.SettingConfig
		fields = "__all__"


class AircraftForExportSerializer(serializers.ModelSerializer):
	AircraftID = serializers.CharField(source='AircraftCode')
	EngineType = serializers.CharField(source='EngType')
	HighPerformance = serializers.BooleanField(source='HighPerf')

	EquipmentType = serializers.SerializerMethodField("get_EquipmentType")
	TypeCode = serializers.SerializerMethodField("get_TypeCode")
	Year = serializers.SerializerMethodField("get_Year")
	GearType = serializers.SerializerMethodField("get_GearType")
	Pressurized = serializers.SerializerMethodField("get_Pressurized")
	TAA = serializers.SerializerMethodField("get_TAA")

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
			'EquipmentType',
			'TypeCode',
			'Year',
			'GearType',
			'Pressurized',
			'TAA'
		)

	def get_EquipmentType(self, obj):
		# Get corresponding field from obj
		# Do manipulation
		# return changed data
		pass

	def get_TypeCode(self, obj):
		# Get corresponding field from obj
		# Do manipulation
		# return changed data
		pass

	def get_Year(self, obj):
		# Get corresponding field from obj
		# Do manipulation
		# return changed data
		pass

	def get_GearType(self, obj):
		# Get corresponding field from obj
		# Do manipulation
		# return changed data
		pass

	def get_Pressurized(self, obj):
		# Get corresponding field from obj
		# Do manipulation
		# return changed data
		pass

	def get_TAA(self, obj):
		# Get corresponding field from obj
		# Do manipulation
		# return changed data
		pass


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