from flask_smorest import Blueprint
from flask.views import MethodView
from db import db

#from models.services_model import ServiceModel
from models.owner_model import Owner

from flask import request


blt = Blueprint('services', __name__, description="This suits for services from all different users")

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

#
# @blt.route('/services')
# def get_all_services():
#     all_services = ServiceModel.query.all()
#     serv_names = []
#     for x in all_services:
#         serv_names.append(x.service_name)
#         # serv_names.append(x)
#
#     return {"Services": serv_names}, 200
#
#
# @blt.route('/services/<string:name>', methods=['POST'])
# def create_service(name):
#     req = request.get_json()
#     servis = ServiceModel(service_name=name, service_description=req['desc'])
#     db.session.add(servis)
#     db.session.commit()
#     return {"Message": f"servis {name} succesfully created"}, 201


