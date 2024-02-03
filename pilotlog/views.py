import os.path
import subprocess
from django.http import HttpResponse
from django.apps import apps
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics as rest_generics
from pilotlog import models as pl_models
from pilotlog import serializers as pl_serializers
from pilotlog.utils import get_serializer_class
from pilotlog.paginations import CustomPagination
from apexive.settings import BASE_DIR, MEDIA_ROOT


@api_view(["GET"])
def import_api(request):
	"""
	Import data to specific database tables in background process
	:param request:
	:return:
	"""
	proc = subprocess.Popen(
		["python3", f"{BASE_DIR}/importer.py",  "--save=1"],
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT
	)
	# out, err = proc.communicate()
	# print(out or err)

	return Response({"success": True, "message": "Importing started."}, status=status.HTTP_202_ACCEPTED)


@api_view(["GET"])
def export_api(reqeust):
	download = reqeust.query_params.get("download")
	filename = reqeust.query_params.get("filename")
	subprocess.Popen(
		["python3", f"{BASE_DIR}/exporter.py", f"--output={MEDIA_ROOT}/{filename}", "--format=json"],
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT
	)

	if download:
		file_path = f"{MEDIA_ROOT}/{filename}"
		if not os.path.exists(file_path):
			return Response(
				{
					"success": False,
					"message": "File not found.",
					"description": f"Either {filename} not exists in DB or export process not finished yet."
				},
				status=status.HTTP_404_NOT_FOUND
			)

		with open(file_path, "rb") as document:
			response = HttpResponse(document, content_type="application/json")
			response["Content-Disposition"] = f'attachment; filename="{filename}"'
			response.status_code = status.HTTP_200_OK
			return response
	return Response({"success": True, "message": "Exporting started."}, status=status.HTTP_202_ACCEPTED)


class AircraftListAPI(rest_generics.ListAPIView):
	model = pl_models.Aircraft
	queryset = pl_models.Aircraft.objects.all()
	serializer_class = pl_serializers.AircraftSerializer
	pagination_class = CustomPagination


class AirfieldListAPI(rest_generics.ListAPIView):
	model = pl_models.Airfield
	queryset = pl_models.Airfield.objects.all()
	serializer_class = pl_serializers.AirfieldSerializer
	pagination_class = CustomPagination


class FlightListAPI(rest_generics.ListAPIView):
	model = pl_models.Flight
	queryset = pl_models.Flight.objects.all()
	serializer_class = pl_serializers.FlightSerializer
	pagination_class = CustomPagination


class PilotListAPI(rest_generics.ListAPIView):
	model = pl_models.Pilot
	queryset = pl_models.Pilot.objects.all()
	serializer_class = pl_serializers.PilotSerializer
	pagination_class = CustomPagination


class QualificationAPI(rest_generics.ListAPIView):
	model = pl_models.Qualification
	queryset = pl_models.Qualification.objects.all()
	serializer_class = pl_serializers.QualificationSerializer
	pagination_class = CustomPagination


class MyQueryAPI(rest_generics.ListAPIView):
	model = pl_models.MyQuery
	queryset = pl_models.MyQuery.objects.all()
	serializer_class = pl_serializers.MyQuerySerializer
	pagination_class = CustomPagination


class MyQueryBuildAPI(rest_generics.ListAPIView):
	model = pl_models.MyQueryBuild
	queryset = pl_models.MyQueryBuild.objects.all()
	serializer_class = pl_serializers.MyQueryBuildSerializer
	pagination_class = CustomPagination


class SettingConfigAPI(rest_generics.ListAPIView):
	model = pl_models.SettingConfig
	queryset = pl_models.SettingConfig.objects.all()
	serializer_class = pl_serializers.SettingConfigSerializer
	pagination_class = CustomPagination


class LimitRulesAPI(rest_generics.ListAPIView):
	model = pl_models.LimitRules
	queryset = pl_models.LimitRules.objects.all()
	serializer_class = pl_serializers.LimitRulesSerializer
	pagination_class = CustomPagination


class ImagePicAPI(rest_generics.ListAPIView):
	model = pl_models.Imagepic
	queryset = pl_models.Imagepic.objects.all()
	serializer_class = pl_serializers.ImagePicSerializer
	pagination_class = CustomPagination


class PilotlogHeaderAPI(rest_generics.ListAPIView):
	model = pl_models.PilotlogHeader
	queryset = pl_models.PilotlogHeader.objects.all()
	serializer_class = pl_serializers.PilotlogHeaderSerializer
	pagination_class = CustomPagination


class ExporterAPI(rest_generics.ListAPIView):
	pagination_class = CustomPagination

	def get_serializer_class(self):
		query = self.request.query_params.get("from")
		self.serializer_class = get_serializer_class(f"{query.capitalize()}Export")
		return self.serializer_class

	def get_queryset(self):
		model_name = self.request.query_params.get("from")
		model_name = model_name.capitalize() if model_name else ""
		model = apps.get_model("pilotlog", model_name)
		self.queryset = model.objects.all()
		return self.queryset
