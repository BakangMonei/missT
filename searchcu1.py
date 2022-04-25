# A script to list rows in a table
#immport the arcpy module
import arcpy
#create a workspace, this is where the data resides
arcpy.env.workspace="C:\Users\cse20-018\Downloads\arcPy_BWA\BWA"
# create variables
shapefile='BWA_adm1.shp'
'''use the searchcursor method. The method has the following syntax
SearchCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})'''
rows=arcpy.SearchCursor(shapefile)
# iterate on the list and print the contents of column NAME_1
for row in rows:
	print(row.getValue('NAME_1'))

