import os

from flask import Flask, Response, request, redirect, url_for
from flask_cors import CORS
# from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.github import make_github_blueprint, github
import json
import logging

import utils.rest_utils as rest_utils
from datetime import datetime
from application_services.SchedulesResource.schedule_service import ScheduleResource
from database_services.RDBService import RDBService as RDBService

from middleware import security

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

app.secret_key = "supersekrit"
blueprint = make_github_blueprint(
    client_id="60427c94b5d59a5b7158",
    client_secret="81d41d4ac72f3c7fc7bbe4053d83a49e3c08b7af",
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

g_bp = app.blueprints.get("google")

@app.before_request
def before_request_fun():
    print("Before request is running!")
    # check_login = security.Secure()
    # result = check_login.security_check_github(request, github, g_bp)
    # print("login_result: ", result)
    # if not result:
    #     print("Going to redirect")
    #     return redirect(url_for("github.login"))


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/login/github")
def google_login():
    return "You are logged in on Github"


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
    app.run(host="0.0.0.0", port=5000)