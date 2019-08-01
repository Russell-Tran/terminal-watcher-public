"""
Practice using the Tadabase API.
This is used as a module by aquavian_refresh_datetime.py
"""
import requests
import datetime
import json
import tadabase_creds as creds # local file "tadabase_creds.py"

appId = creds.appId
appKey = creds.appKey
appSecret = creds.appSecret

# See a list of tables in your Tadabase app
def print_all_tables_in_app():
	url = 'https://api.tadabase.io/api/v1/data-tables'
	headers = {
	  'X-Tadabase-App-id': appId,
	  'X-Tadabase-App-Key': appKey,
	  'X-Tadabase-App-Secret': appSecret
	}
	payload = {}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=None)
	print("See a list of tables in your app:")
	print(response.text)

# See a list of fields inside a table
def print_all_fields_inside_table(table_id):
	url = 'https://api.tadabase.io/api/v1/data-tables/{tableId}/fields'.format(tableId=table_id)
	headers = {
	  'X-Tadabase-App-id': appId,
	  'X-Tadabase-App-Key': appKey,
	  'X-Tadabase-App-Secret': appSecret
	}
	payload = {}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=None)
	print("See a list of fields inside a table:")
	print(response.text)

# Returns an array of dictionaries, where each dictionary represents a row in the table
# And maps 'field_xx' : 'value'
def get_all_records(table_id):
	url = 'https://api.tadabase.io/api/v1/data-tables/{tableId}/records'.format(tableId=table_id)
	payload = {}
	headers = {
	  'X-Tadabase-App-id': appId,
	  'X-Tadabase-App-Key': appKey,
	  'X-Tadabase-App-Secret': appSecret
	}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=None)
	valid_json_string = "[{}]".format(response.text)
	data = json.loads(valid_json_string)
	return data[0]["items"]

def get_array_of_row_ids(table_id):
	all_records = get_all_records(table_id)
	row_ids = []
	for row in all_records:
		row_ids.append(row['id'])
	return row_ids

def update_single_record(table_id, record_id, field_id, field_value, print_response=True):
	url = 'https://api.tadabase.io/api/v1/data-tables/{tableId}/records/{recordId}'.format(tableId=table_id, recordId=record_id)
	payload = {field_id: field_value}
	files = {}
	headers = {
	  'X-Tadabase-App-id': appId,
	  'X-Tadabase-App-Key': appKey,
	  'X-Tadabase-App-Secret': appSecret,
	  'Content-Type': 'application/x-www-form-urlencoded'
	}
	response = requests.request('POST', url, headers = headers, data = payload, files = files, allow_redirects=False, timeout=None)
	if print_response:
		print(response.text)

# According to Tadabase API spec for datetime
def generate_now_string():
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%d %H:%M:%S")

# Given a table_id and a field_id for a Tadabase "datetime" field,
# Updates every row in the table to the current time.
def update_all_datetime_now(table_id, field_id):
	row_ids = get_array_of_row_ids(table_id)
	for row_id in row_ids:
		now_string = generate_now_string()
		update_single_record(table_id=table_id, record_id=row_id, field_id=field_id, field_value=now_string)

if __name__ == '__main__':
	api_practice_table_id = 'q3kjZVj6Vb' 
	api_practice_datetime_field_id = 'field_86'
	update_all_datetime_now(table_id=api_practice_table_id, field_id=api_practice_datetime_field_id)

