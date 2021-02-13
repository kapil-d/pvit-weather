import time
from weppy import App, request
from weppy.orm import Model, Field
from weppy.orm import Database

app = App(__name__)

class Reading(Model):
    """ Weather Reading """
    station_id = Field.text()
    date = Field.text()
    temperature = Field.float()

    validation = {
        'station_id': {'presence': True},
        'date': {'presence': True},
        'temperature': {'presence': True}
    }

db = Database(app, auto_migrate=True)    
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
    readings = Reading.all().select()
    return dict(readings=readings)

@app.route("/submit")
def submit():
    station_id = request.query_params.station
    datetime = request.query_params.datetime
    temperature = request.query_params.temp

    reading = Reading.create(
        station_id = station_id,
        date = datetime,
        temperature = temperature)
    db.commit()

