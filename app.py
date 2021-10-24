from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging

from application_services.SchedulesResource.schedule_service import ScheduleResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_schedule():
    return '<u>Hello this is the schedule microservice!</u>'


@app.route('/schedules', methods = ['POST','GET'])
def get_schemes():
    if request.method == 'GET':
        res = ScheduleResource.get_by_template(None)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp
    elif request.method == 'POST':
        generate_row = ScheduleResource.create_schedule(request.json)
        return '<u>Successfully post new schemes!</u>'


@app.route('/schedules/<prefix>', methods = ['POST','GET','DELETE','UPDATE'])
def order_id(prefix):
    if request.method == 'GET':
        res = ScheduleResource.get_by_schedule_id(prefix)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
        return rsp


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
