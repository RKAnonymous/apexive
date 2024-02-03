from django.contrib import admin
from pilotlog import models

admin.site.register(models.PilotlogHeader)
admin.site.register(models.Airfield)
admin.site.register(models.Aircraft)
admin.site.register(models.Pilot)
admin.site.register(models.Flight)
admin.site.register(models.MyQuery)
admin.site.register(models.MyQueryBuild)
admin.site.register(models.Qualification)
admin.site.register(models.SettingConfig)
admin.site.register(models.LimitRules)
admin.site.register(models.Imagepic)
