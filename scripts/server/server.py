#!/usr/bin/env python3
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask.views import MethodView, View

from read_write import build_gtfs_file

#HOST_IP = "0.0.0.0"
#HOST_PORT = "4040"


def create_app():
    app = Flask(__name__)
    CORS(app)

    register_views(app)

    return app


def register_views(app):
    app.add_url_rule('/', view_func=ServerHome.as_view('get_homepage'))
    app.add_url_rule('/upload_file', view_func=DataUpload.as_view('upload_file'))


class ServerHome(View):
    def dispatch_request(self):
        return "<h1>GTFSVisual Server</h1>"


class DataUpload(MethodView):
    def post(self):
        for name in request.files:
            file_obj = request.files[name]
            file_name = file_obj.filename.split(".")[0]
            text = file_obj.read().decode("utf-8").split("\n")

            gtfs_file = build_gtfs_file(file_name, text)

        #text = request.data.decode("utf-8").split("\n")

        return jsonify(gtfs_file.json())
