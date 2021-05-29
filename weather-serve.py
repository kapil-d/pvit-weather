import time
import datetime
from weppy import App, request
from weppy.orm import Model, Field
from weppy.orm import Database

app = App(__name__)

allowed_stations = ['KD1', 'PRM', 'PVH', 'SMA']

class Reading(Model):
    """ Weather Reading """
    station_id = Field.text()
    date = Field.datetime()
    temperature = Field.float()

    validation = {
        'station_id': {'presence': True},
        'date': {'presence': True},
        'temperature': {'presence': True}
    }

db = Database(app, auto_migrate=False)
db.define_models(Reading)

app.pipeline = [
    db.pipe
]

@app.command('setup')
def setup():
    reading = Reading.create(
        station_id = 'XXX',
        date = time.asctime(),
        temperature = 73.0
    )
    print(reading)
    db.commit()

@app.route("/")
def index():
    readings = Reading.all().select(orderby=~Reading.date)
    return dict(readings=readings)

@app.route("/submit")
def submit():
    station_id = request.query_params.station
    date_time = request.query_params.datetime
    temperature = request.query_params.temp

    if station_id in allowed_stations:
        reading = Reading.create(
            station_id = station_id,
            date = datetime.datetime.strptime(date_time, "%a %b %d %H:%M:%S %Y"),
            temperature = temperature)
        db.commit()
