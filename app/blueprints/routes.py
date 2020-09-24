from flask import request, jsonify, Blueprint

from app import db
from ..input_schema import schema_message
from ..utils import validate, clean_dict
from ..models import Message

import datetime
import re

api_v1 = Blueprint('api/v1', __name__)


@api_v1.route('message', methods=['POST'])
def post_message():
		try:
				email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
				cel_phone_regex = '^[1-9]{2}(?:[2-8]|9[1-9])[0-9]{3}[0-9]{4}$'

				payload = request.get_json(silent=True)

				if validate(payload, schema_message) is False:
						return jsonify({'error': {'message': 'invalid value(s)'}}), 400

				clean_dict(payload)

				# Verify if required keys was passed
				if not payload['recipient']:
						return jsonify({'error': {'message': 'recipient is a required key'}}), 400
				if not payload['message']:
						return jsonify({'error': {'message': 'message is a required key'}}), 400
				if not payload['date_time']:
						return jsonify({'error': {'message': 'date_time is a required key'}}), 400
	
				# Verify the if date/hour is bigger the the current
				if datetime.datetime.now() > datetime.datetime.strptime(payload['date_time'], '%Y-%m-%d %H:%M:%S'):
						return jsonify({'error': {'message': 'the date / hour cannot be smaller than date / hour of registration moment'}}), 400

				# Verify if recipient value is valid
				if re.search(email_regex, payload['recipient']) or re.search(cel_phone_regex, payload['recipient']):
						message = Message(recipient=payload['recipient'],
									message=payload['message'],
									date_time=payload['date_time'])
						db.session.add(message)
						db.session.commit()

						return jsonify(
							{'id': message.id, 'recipient': message.recipient, 'message': message.message, 'date_time': str(message.date_time),
							'status': message.status}), 201

				return jsonify({'error': {'message': 'recipient must be a valid email or an valid cel phone'}}), 400

		except Exception as e:
				print('ERROR: {}'.format(e))
				return jsonify({'error': {'message': 'server was unable to process the request'}}), 400

@api_v1.route('message', methods=['GET'])
def get_messages():
		try:
				messages = Message.query.all()
				return jsonify({"messages": [message.to_dict() for message in messages]}), 200
		except Exception as e:
				print('ERROR: {}'.format(e))
				return jsonify({'error': {'message': 'server was unable to process the request'}}), 400

@api_v1.route('message/<id>', methods=['GET'])
def get_message(id):
		try:
				data = Message.query.get(id)
				return jsonify(data.to_dict()), 200
		except Exception as e:
				print('ERROR: {}'.format(e))
				return jsonify({'error': {'message': 'server was unable to process the request'}}), 400

@api_v1.route('message/<id>', methods=['PUT'])
def put_message(id):
		try:
				email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
				cel_phone_regex = '^[1-9]{2}(?:[2-8]|9[1-9])[0-9]{3}[0-9]{4}$'
				message = Message.query.get(id)

				payload = request.get_json(silent=True)

				message.status = payload['status']

				payload.pop('status')

				clean_dict(payload)
				
				# Verify if recipient value is valid
				if re.search(email_regex, payload['recipient']) or re.search(cel_phone_regex, payload['recipient']):
						message.recipient	= payload['recipient']
				else:
						return jsonify({'error': {'message': 'recipient must be a valid email or an valid cel phone'}}), 400
				
				message.message = payload['message']
				
				if message.status == False:
					# Verify the if date/hour is bigger the the current
					if datetime.datetime.now() > datetime.datetime.strptime(payload['date_time'], '%Y-%m-%d %H:%M:%S'):
							return jsonify({'error': {'message': 'the date / hour cannot be smaller than date / hour of registration moment'}}), 400
				else:
						message.date_time = payload['date_time']

				db.session.commit()		
				return jsonify(
							{'id': message.id, 'recipient': message.recipient, 'message': message.message, 'date_time': str(message.date_time),
							'status': message.status}), 200

		except Exception as e:
				print('ERROR: {}'.format(e))
				return jsonify({'error': {'message': 'server was unable to process the request'}}), 400

@api_v1.route('message/<id>', methods=['DELETE'])
def delete_message(id):
		try:		
				Message.query.filter_by(id=id).delete()
				db.session.commit()
				data = {'message': 'message deleted'}
				return jsonify(data), 200

		except Exception as e:
				print('ERROR: {}'.format(e))
				return jsonify({'error': {'message': 'server was unable to process the request'}}), 400
