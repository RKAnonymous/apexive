from django.urls import path
from pilotlog import views as pl_views


urlpatterns = [
	path("import/", pl_views.import_api, name="import"),
	path("export/", pl_views.export_api, name="export"),
	path("main/", pl_views.PilotlogHeaderAPI.as_view(), name="pilotlog"),
	path("aircraft/", pl_views.AircraftListAPI.as_view(), name="aircraft"),
	path("airfield/", pl_views.AirfieldListAPI.as_view(), name="airfield"),
	path("pilot/", pl_views.PilotListAPI.as_view(), name="pilot"),
	path("flight/", pl_views.FlightListAPI.as_view(), name="flight"),
	path("qualification/", pl_views.QualificationAPI.as_view(), name="qualification"),
	path("my-query/", pl_views.MyQueryAPI.as_view(), name="query"),
	path("my-query-build/", pl_views.MyQueryBuildAPI.as_view(), name="build"),
	path("limit-rules/", pl_views.LimitRulesAPI.as_view(), name="limit"),
	path("image/", pl_views.ImagePicAPI.as_view(), name="image"),
	path("setting-config/", pl_views.SettingConfigAPI.as_view(), name="config"),
	path("export/", pl_views.ExporterAPI.as_view(), name="config"),
]
