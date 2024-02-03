# Apexive Coding Assignment

## Importer
Data importer from `import - politlog_mcc.json` file.

#### What should trigger the importer?
    1. Manual usage of the script in views or another module
    2. Generate API endpoint to invoke the script 
    3. CRON job or Airflow DAG which executes the script at a specified time

Import class generated to interact with `import - politlog_mcc.json` file.
The exact same script used in `pilotlog` app to save data from file.
API view executes the script in background and returns `202 Accepted` status.
Imported data can be checked by requesting List API endpoints to corresponding table.

#### How Importer works?
    1. Read source file.                                                     =>   self.read
    2. Clean by replacing unnecessary characters. E.g. (/, \, ', ")          =>   self.read
    3. Get table names from header objects.                                  =>   self.get_tables
    4. Filter data by table names.                                           =>   self.filter_by
    5. Create insertion query according to table names, columns and values   =>   self.insert_query
    6. Save header data and table data.                                      =>   self.push
    
    - save cleaned json data                                                 =>   self.prettify
    - interactive shell loader                                               =>   self.loader
    - database config parameters parser                                      =>   self.get_db_conf

#### Flags/Options
    -s    --source    Source file with JSON formatted data.
	-o    --output    Destination file to save data in more python friendly structure.
	-d    --db-conf   Database config file(JSON) to push data to DB.
	      --save      Flag to save data to default db.
  


## Politlog app
DB connector to save data from politlog_mcc.json to Postgres in a structured way.

#### Endpoints

    +-----------------+-----------------------------------+-------------------+--------------------------------------+
    | URL             |     OUTCOME                       |    SUCCESS        |      RESULT DESCRIPTION              |
    +-----------------+-----------------------------------+-------------------+--------------------------------------+
    | import/         |   - run importer                  |   - 202 Accepted  |      Request accepted to import data |
    | aircraft/       |   - list of Aircraft objects      |   - 200 OK        |      Paginated list of objects       |
    | airfield/       |   - list of Airfield objects      |   - 200 OK        |      Paginated list of objects       |
    | flight/         |   - list of Flight objects        |   - 200 OK        |      Paginated list of objects       |
    | image/          |   - list of ImagePic objects      |   - 200 OK        |      Paginated list of objects       |
    | limit-rules/    |   - list of LimitRules objects    |   - 200 OK        |      Paginated list of objects       |
    | my-query/       |   - list of myQuery objects       |   - 200 OK        |      Paginated list of objects       |
    | my-query-build/ |   - list of myQueryBuild objects  |   - 200 OK        |      Paginated list of objects       |
    | pilot/          |   - list of Pilot objects         |   - 200 OK        |      Paginated list of objects       |
    | qualification/  |   - list of Qualification objects |   - 200 OK        |      Paginated list of objects       |
    | setting-config/ |   - list of SettingConfig objects |   - 200 OK        |      Paginated list of objects       |
    +-----------------+-----------------------------------+-------------------+--------------------------------------+


## Exporter
Data exporter in the format specified in `export-logbook_template.csv`

#### What should trigger the exporter?
    1. Manual usage of the script in views or another module
    2. Generate API endpoint to invoke the script
    3. CRON job or Airflow DAG which executes the script at a specified time

#### How Exporter works?
    1. Read template file.                                                   =>   self.get_template
    2. Create select query up to table names and columns.                    =>   self.select_query
    3. Pull data from database.                                              =>   self.get_data
    4. Reformat data according to template file.                             =>   self.reformat

    - save data into custom formated file                                    =>   self.output

#### Flags/Options
    -o      --output       Destination file to save file
	-f      --format       Destination file format to save file
	-t      --template     Data structure template file.

Due to insufficient information on data fields provided in `export-logbook_template.csv`,
currently, it is impossible to make exporter script work properly.
Fields provided in the `.csv` are not compatible with the fields `.json`.
More precise instruction is needed to manipulate with data fields saved in DB.


### NOTES
- In order to avoid NOT NULL validation error of DB all fields set blank=True null=True.
  Because fields are not strictly the same through the objects in `.json`.


### Usage

1. Get the source code:
    
        git clone git@github.com:RKAnonymous/apexive.git

2. Get to the project root directory:
      
        cd apexive

3. Generate virtual environment and activate it:
  
        python3 -m venv venv
        source venv/bin/activate or . venv/bin/activate

4. Install the dependencies:

        pip install -r requirements.txt

5. Create .env file and have all private information in it:

        SECRET_KEY, DEBUG, ALLOWED_HOSTS - for django project
        SQL_* - for database parameters
        ...

6. Create database and write the parameters to .env file:
      
        SQL_DATABASE=your_db_name
        SQL_USER=your_db_user
        SQL_PASSWORD=your_db_password
        SQL_HOST=your_db_host or localhost
        SQL_PORT=your_db_port or 5432

### Running the Importer and Exporter scripts

7. Run Importer:
  
        python3 importer.py [OPTIONS]

8. Run Exporter:

        python3 exporter.py [OPTIONS]