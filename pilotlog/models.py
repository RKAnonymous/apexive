from django.db import models


class Aircraft(models.Model):
	Fin = models.CharField(max_length=255, blank=True, null=True)
	Sea = models.BooleanField(default=False, blank=True, null=True)
	TMG = models.BooleanField(default=False, blank=True, null=True)
	Efis = models.BooleanField(default=False, blank=True, null=True)
	FNPT = models.IntegerField(default=0, blank=True, null=True)
	Make = models.CharField(max_length=255, blank=True, null=True)
	Run2 = models.BooleanField(default=False, blank=True, null=True)
	Class = models.IntegerField(blank=True, null=True)
	Model = models.CharField(max_length=255, blank=True, null=True)
	Power = models.IntegerField(blank=True, null=True)
	Seats = models.IntegerField(blank=True, null=True)
	Active = models.BooleanField(blank=True, null=True)
	Kg5700 = models.BooleanField(blank=True, null=True)
	Rating = models.CharField(max_length=50, blank=True, null=True)
	Company = models.CharField(max_length=255, blank=True, null=True)
	Complex = models.BooleanField(blank=True, null=True)
	CondLog = models.IntegerField(blank=True, null=True)
	EngType = models.IntegerField(blank=True, null=True)
	EngGroup = models.IntegerField(blank=True, null=True)
	FavList = models.BooleanField(blank=True, null=True)
	Category = models.IntegerField(blank=True, null=True)
	HighPerf = models.BooleanField(blank=True, null=True)
	SubModel = models.CharField(max_length=50, blank=True, null=True)
	Aerobatic = models.BooleanField(blank=True, null=True)
	RefSearch = models.CharField(max_length=50, blank=True, null=True)
	Reference = models.CharField(max_length=50, blank=True, null=True)
	Tailwheel = models.BooleanField(blank=True, null=True)
	DefaultApp = models.IntegerField(blank=True, null=True)
	DefaultLog = models.IntegerField(blank=True, null=True)
	DefaultOps = models.IntegerField(blank=True, null=True)
	DeviceCode = models.IntegerField(blank=True, null=True)
	AircraftCode = models.CharField(max_length=40, blank=True, null=True)  # AircraftID
	DefaultLaunch = models.IntegerField(blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)  # NOTE: DateTimeField()

	def __str__(self):
		return self.Make or self.Model


class Flight(models.Model):
	PF = models.BooleanField(blank=True, null=True)
	Pax = models.IntegerField(blank=True, null=True)
	Fuel = models.IntegerField(blank=True, null=True)
	Cargo = models.IntegerField(blank=True, null=True)
	DeIce = models.BooleanField(blank=True, null=True)
	Route = models.CharField(max_length=50, blank=True, null=True)
	ToDay = models.IntegerField(blank=True, null=True)
	minU1 = models.IntegerField(blank=True, null=True)
	minU2 = models.IntegerField(blank=True, null=True)
	minU3 = models.IntegerField(blank=True, null=True)
	minU4 = models.IntegerField(blank=True, null=True)
	minXC = models.IntegerField(blank=True, null=True)
	ArrRwy = models.CharField(max_length=10, blank=True, null=True)
	DepRwy = models.CharField(max_length=10, blank=True, null=True)
	LdgDay = models.IntegerField(blank=True, null=True)
	LiftSW = models.IntegerField(blank=True, null=True)
	P1Code = models.CharField(max_length=40, blank=True, null=True)
	P2Code = models.CharField(max_length=40, blank=True, null=True)
	P3Code = models.CharField(max_length=40, blank=True, null=True)
	P4Code = models.CharField(max_length=40, blank=True, null=True)
	Report = models.CharField(max_length=255, blank=True, null=True)
	TagOps = models.CharField(max_length=50, blank=True, null=True)
	ToEdit = models.BooleanField(blank=True, null=True)
	minAIR = models.IntegerField(blank=True, null=True)
	minCOP = models.IntegerField(blank=True, null=True)
	minIFR = models.IntegerField(blank=True, null=True)
	minIMT = models.IntegerField(blank=True, null=True)
	minPIC = models.IntegerField(blank=True, null=True)
	minREL = models.IntegerField(blank=True, null=True)
	minSFR = models.IntegerField(blank=True, null=True)
	ArrCode = models.CharField(max_length=40, blank=True, null=True)
	DateUTC = models.DateField(blank=True, null=True)
	DepCode = models.CharField(max_length=40, blank=True, null=True)
	HobbsIn = models.IntegerField(blank=True, null=True)
	Holding = models.IntegerField(blank=True, null=True)
	Pairing = models.CharField(max_length=50, blank=True, null=True)
	Remarks = models.CharField(max_length=50, blank=True, null=True)
	SignBox = models.IntegerField(blank=True, null=True)
	ToNight = models.IntegerField(blank=True, null=True)
	UserNum = models.IntegerField(blank=True, null=True)
	minDUAL = models.IntegerField(blank=True, null=True)
	minEXAM = models.IntegerField(blank=True, null=True)
	CrewList = models.CharField(max_length=50, blank=True, null=True)
	DateBASE = models.DateField(blank=True, null=True)
	FuelUsed = models.IntegerField(blank=True, null=True)
	HobbsOut = models.IntegerField(blank=True, null=True)
	LdgNight = models.IntegerField(blank=True, null=True)
	NextPage = models.BooleanField(blank=True, null=True)
	TagDelay = models.CharField(max_length=50, blank=True, null=True)
	Training = models.CharField(max_length=50, blank=True, null=True)
	UserBool = models.BooleanField(blank=True, null=True)
	UserText = models.CharField(max_length=50, blank=True, null=True)
	minINSTR = models.IntegerField(blank=True, null=True)
	minNIGHT = models.IntegerField(blank=True, null=True)
	minPICUS = models.IntegerField(blank=True, null=True)
	minTOTAL = models.IntegerField(blank=True, null=True)
	ArrOffset = models.IntegerField(blank=True, null=True)
	DateLOCAL = models.DateField(blank=True, null=True)
	DepOffset = models.IntegerField(blank=True, null=True)
	TagLaunch = models.CharField(max_length=50, blank=True, null=True)
	TagLesson = models.CharField(max_length=50, blank=True, null=True)
	ToTimeUTC = models.IntegerField(blank=True, null=True)
	ArrTimeUTC = models.IntegerField(blank=True, null=True)
	BaseOffset = models.IntegerField(blank=True, null=True)
	DepTimeUTC = models.IntegerField(blank=True, null=True)
	FlightCode = models.CharField(max_length=40, blank=True, null=True)
	LdgTimeUTC = models.IntegerField(blank=True, null=True)
	FuelPlanned = models.IntegerField(blank=True, null=True)
	NextSummary = models.BooleanField(blank=True, null=True)
	TagApproach = models.CharField(max_length=10, blank=True, null=True)
	AircraftCode = models.CharField(max_length=40, blank=True, null=True)
	ArrTimeSCHED = models.IntegerField(blank=True, null=True)
	DepTimeSCHED = models.IntegerField(blank=True, null=True)
	FlightNumber = models.CharField(max_length=10, blank=True, null=True)
	FlightSearch = models.CharField(max_length=40, blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.FlightCode


class Airfield(models.Model):
	City = models.CharField(max_length=125, blank=True, null=True)
	AFCat = models.IntegerField(blank=True, null=True)
	AFFAA = models.CharField(max_length=125, blank=True, null=True)
	Notes = models.TextField(max_length=500, blank=True, null=True)
	AFCode = models.CharField(max_length=40, blank=True, null=True)
	AFIATA = models.CharField(max_length=125, blank=True, null=True)
	AFICAO = models.CharField(max_length=50, blank=True, null=True)
	AFName = models.CharField(max_length=125, blank=True, null=True)
	TZCode = models.IntegerField(blank=True, null=True)
	Latitude = models.IntegerField(blank=True, null=True)
	ShowList = models.BooleanField(blank=True, null=True)
	UserEdit = models.BooleanField(blank=True, null=True)
	AFCountry = models.IntegerField(blank=True, null=True)
	Longitude = models.IntegerField(blank=True, null=True)
	NotesUser = models.CharField(max_length=125, blank=True, null=True)
	RegionUser = models.IntegerField(blank=True, null=True)
	ElevationFT = models.IntegerField(blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.AFName


class Pilot(models.Model):
	Notes = models.TextField(max_length=500, blank=True, null=True)
	Active = models.BooleanField(blank=True, null=True)
	Company = models.CharField(max_length=50, blank=True, null=True)
	FavList = models.BooleanField(blank=True, null=True)
	UserAPI = models.CharField(max_length=125, blank=True, null=True)
	Facebook = models.CharField(max_length=125, blank=True, null=True)
	LinkedIn = models.CharField(max_length=125, blank=True, null=True)
	PilotRef = models.CharField(max_length=125, blank=True, null=True)
	PilotCode = models.CharField(max_length=60, blank=True, null=True)
	PilotName = models.CharField(max_length=50, blank=True, null=True)
	PilotEMail = models.CharField(max_length=125, blank=True, null=True)
	PilotPhone = models.CharField(max_length=50, blank=True, null=True)
	Certificate = models.CharField(max_length=50, blank=True, null=True)
	PhoneSearch = models.CharField(max_length=125, blank=True, null=True)
	PilotSearch = models.CharField(max_length=125, blank=True, null=True)
	RosterAlias = models.CharField(max_length=125, blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.PilotName


class Qualification(models.Model):
	QCode = models.CharField(max_length=125, blank=True, null=True)
	RefExtra = models.IntegerField(blank=True, null=True)
	RefModel = models.CharField(max_length=10, blank=True, null=True)
	Validity = models.IntegerField(blank=True, null=True)
	DateValid = models.CharField(max_length=10, blank=True, null=True)
	QTypeCode = models.IntegerField(blank=True, null=True)
	DateIssued = models.CharField(max_length=10, blank=True, null=True)
	MinimumQty = models.IntegerField(blank=True, null=True)
	NotifyDays = models.IntegerField(blank=True, null=True)
	RefAirfield = models.CharField(max_length=125, blank=True, null=True)
	MinimumPeriod = models.IntegerField(blank=True, null=True)
	NotifyComment = models.CharField(max_length=125, blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)


class MyQuery(models.Model):
	Name = models.CharField(max_length=255, blank=True, null=True)
	mQCode = models.CharField(max_length=255, blank=True, null=True)
	QuickView = models.BooleanField(blank=True, null=True)
	ShortName = models.CharField(max_length=255, blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)
	
	class Meta:
		verbose_name = "Query"
		verbose_name_plural = "Queries"


class MyQueryBuild(models.Model):
	Build1 = models.CharField(max_length=60, blank=True, null=True)
	Build2 = models.IntegerField(blank=True, null=True)
	Build3 = models.IntegerField(blank=True, null=True)
	Build4 = models.CharField(max_length=60, blank=True, null=True)
	mQCode = models.CharField(max_length=60, blank=True, null=True)
	mQBCode = models.CharField(max_length=60, blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)
	
	class Meta:
		verbose_name = "Build"
		verbose_name_plural = "Builds"


class SettingConfig(models.Model):
	Data = models.CharField(max_length=50, blank=True, null=True)
	Name = models.CharField(max_length=50, blank=True, null=True)
	Group = models.CharField(max_length=50, blank=True, null=True)
	ConfigCode = models.IntegerField(blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)
	
	class Meta:
		verbose_name = "Config"
		verbose_name_plural = "Configs"


class LimitRules(models.Model):
	LTo = models.CharField(max_length=16, blank=True, null=True)
	LFrom = models.CharField(max_length=16, blank=True, null=True)
	LType = models.IntegerField(blank=True, null=True)
	LZone = models.IntegerField(blank=True, null=True)
	LMinutes = models.IntegerField(blank=True, null=True)
	LimitCode = models.CharField(max_length=60, blank=True, null=True)
	LPeriodCode = models.IntegerField(blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)
	
	class Meta:
		verbose_name = "Limit rule"
		verbose_name_plural = "Limit rules"


class Imagepic(models.Model):
	FileExt = models.CharField(max_length=10, blank=True, null=True)
	ImgCode = models.CharField(max_length=40, blank=True, null=True)
	FileName = models.CharField(max_length=40, blank=True, null=True)
	LinkCode = models.CharField(max_length=40, blank=True, null=True)
	Img_Upload = models.BooleanField(blank=True, null=True)
	Img_Download = models.BooleanField(blank=True, null=True)
	Record_Modified = models.IntegerField(blank=True, null=True)
	
	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"


class PilotlogHeader(models.Model):
	user_id = models.IntegerField(blank=True, null=True)
	table = models.CharField(max_length=255, blank=True, null=True)
	guid = models.CharField(max_length=255, blank=True, null=True)
	platform = models.IntegerField(blank=True, null=True)
	modified = models.IntegerField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.table)
