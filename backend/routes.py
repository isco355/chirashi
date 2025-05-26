from flask import Flask, request, jsonify,Blueprint
from db.database import Flier
from helpers.orc import extractTextFromImage
import json

routes = Blueprint('flier', __name__)

@routes.get("/fliers")
def hello_world():
    all=list(Flier.select().dicts())
    print(all)
    return jsonify(all)

@routes.post("/flier")
def createFlier():
    output = extractTextFromImage(request)
    flier =Flier(**output)
    flier.save()
    return output

@routes.get('/flier/<int:flier_id>')
def viewFlier(flier_id):
    temp_flier =Flier.get(Flier.id == flier_id)
    return jsonify(temp_flier.to_json())

@routes.delete('/flier/<int:flier_id>')
def deleteFlier(flier_id):
    temp_flier =Flier.get(Flier.id == flier_id)
    temp_flier.delete_instance()
    return jsonify({"message": f"flier deleted{flier_id}"})
