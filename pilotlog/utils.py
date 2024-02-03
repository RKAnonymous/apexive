from pilotlog import serializers as pl_serializers


def get_serializer_class(class_name):
	serializers = {
		"Aircraft": pl_serializers.AircraftSerializer,
		"Airfield": pl_serializers.AirfieldSerializer,
		"Flight": pl_serializers.FlightSerializer,
		"LimitRules": pl_serializers.LimitRulesSerializer,
		"ImagePic": pl_serializers.ImagePicSerializer,
		"Pilot": pl_serializers.PilotSerializer,
		"MyQuery": pl_serializers.MyQuerySerializer,
		"MyQueryBuild": pl_serializers.MyQueryBuildSerializer,
		"Qualification": pl_serializers.QualificationSerializer,
		"SettingConfig": pl_serializers.SettingConfigSerializer,
		"AircraftExport": pl_serializers.AircraftForExportSerializer
	}

	return serializers.get(class_name)
