from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging

import utils.rest_utils as rest_utils
from datetime import datetime
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


@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="app/json")
    return rsp


@app.route('/schedules', methods=['GET'])
def get_schedules():
    inputs = rest_utils.RESTContext(request)
    template = inputs.args
    res = ScheduleResource.get_by_template(template)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.get_json()
    res = ScheduleResource.create_schedule(data)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/schedules/<schedule_id>', methods=['GET'])
def get_schedule_by_id(schedule_id):
    res = ScheduleResource.get_by_schedule_id(schedule_id)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/schedules/<schedule_id>', methods=['PUT'])
def update_schedule_by_id(schedule_id):
    data = request.get_json()
    res = ScheduleResource.update({"scheduledId": schedule_id}, data)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/schedules/<schedule_id>', methods=['DELETE'])
def order_id(schedule_id):
    res = ScheduleResource.delete({"scheduledId": schedule_id})
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
