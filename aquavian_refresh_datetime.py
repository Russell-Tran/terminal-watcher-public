"""
Run this script, and it will update the "Data last updated" field for the actual
Aquavian Freight company's Containers data table.
It updates it to now.
"""
import tadabase_practice # local file "tadabase_practice.py"

# tadabase_practice.print_all_tables_in_app()
# Output: ...{"id":"lGArg7rmR6","name":"Containers"}...
aquavian_containers_table_id = "lGArg7rmR6"

# tadabase_practice.print_all_fields_inside_table(aquavian_containers_table_id)
# Output: ...{"slug":"field_79","name":"Data Last Updated","type":"Date\/Time"}...
aquavian_datetime_field_id = "field_79"

if __name__ == '__main__':
	print("The time is:")
	print(tadabase_practice.generate_now_string())
	tadabase_practice.update_all_datetime_now(table_id=aquavian_containers_table_id, 
		field_id=aquavian_datetime_field_id)