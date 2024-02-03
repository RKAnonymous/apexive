from django.urls import path, include
from pilotlog import views as pl_views


urlpatterns = [
	path("import/", pl_views.import_api, name="import"),
	path("export/", pl_views.export_api, name="export"),
	path("main/", pl_views.PilotlogHeaderAPI.as_view(), name="pilotlog"),
	path("aircraft/", include([
		path("list/", pl_views.AircraftViewSet.as_view({"get": "list"}), name="aircraft_list"),
		path("create/", pl_views.AircraftViewSet.as_view({"post": "create"}), name="aircraft_create"),
		path("detail/<int:pk>/", pl_views.AircraftViewSet.as_view({"get": "retrieve"}), name="aircraft_detail"),
		path("update/<int:pk>/", include([
			path("",  pl_views.AircraftViewSet.as_view({"put": "update"}), name="aircraft_update"),
			path("partial/",  pl_views.AircraftViewSet.as_view({"patch": "partial_update"}), name="aircraft_update_partial"),
		])),
		path("delete/<int:pk>/", pl_views.AircraftViewSet.as_view({"delete": "destroy"}), name="aircraft_delete"),
	])),
	path("airfield/", pl_views.AirfieldListAPI.as_view(), name="airfield"),
	path("pilot/", pl_views.PilotListAPI.as_view(), name="pilot"),
	path("flight/", pl_views.FlightListAPI.as_view(), name="flight"),
	path("qualification/", pl_views.QualificationAPI.as_view(), name="qualification"),
	path("my-query/", pl_views.MyQueryAPI.as_view(), name="query"),
	path("my-query-build/", pl_views.MyQueryBuildAPI.as_view(), name="build"),
	path("limit-rules/", pl_views.LimitRulesAPI.as_view(), name="limit"),
	path("image/", pl_views.ImagePicAPI.as_view(), name="image"),
	path("setting-config/", pl_views.SettingConfigAPI.as_view(), name="config"),
]
